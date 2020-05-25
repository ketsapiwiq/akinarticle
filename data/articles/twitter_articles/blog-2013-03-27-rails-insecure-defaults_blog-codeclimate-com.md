---
title: "Rails' Insecure Defaults"
url: http://blog.codeclimate.com/blog/2013/03/27/rails-insecure-defaults/
keywords: rails,server,default,developers,production,practice,yaml,defaults,user,application,insecure,data
---
Rails\' Insecure Defaults {#rails-insecure-defaults .article__title}
=========================

13 Security Gotchas You Should Know About

[Bryan Helmkamp](//twitter.com/brynary) on

**Update:** If you're interested in this, you may want to check out our new [free, 1-month email course about Rails security](http://railssecurity.com/).

Secure defaults are critical to building secure systems. If a developer must take explicit action to enforce secure behavior, eventually even an experienced developer will forget to do so. For this reason, security experts say:

> "Insecure by default is insecure."

Rails' reputation as a relatively secure Web framework is well deserved. Out-of-the-box, there is protection against many common attacks: cross site scripting (XSS), cross site request forgery (CSRF) and SQL injection. Core members are knowledgeable and genuinely concerned with security.

However, there are places where the default behavior could be more secure. This post explores potential security issues in Rails 3 that are fixed in Rails 4, as well as some that are still risky. I hope this post will help you secure your own apps, as well as inspire changes to Rails itself.

Rails 3 Issues
--------------

Let's begin by looking at some Rails 3 issues that are resolved in master. The Rails team deserves credit for addressing these, but they are worth noting since many applications will be running on Rails 2 and 3 for years to come.

[]{#match-routes}

### 1. CSRF via Leaky \#match Routes

Here is an example taken directly from the Rails 3 generated `config/routes.rb` file:

``` {.highlight .ruby}
WebStore::Application.routes.draw do
  # Sample of named route:
  match 'products/:id/purchase' => 'catalog#purchase',
    :as => :purchase
  # This route can be invoked with
  # purchase_url(:id => product.id)
end
```

This has the effect of routing the `/products/:id/purchase` path to the `CatalogController#purchase` method for all HTTP verbs (`GET`, `POST`, etc). The problem is that Rails' cross site request forgery (CSRF) protection does not apply to `GET` requests. You can see this in the method to enforce CSRF protection:

``` {.highlight .ruby}
def verified_request?
  !protect_against_forgery? ||
  request.get? ||
  form_authenticity_token ==
    params[request_forgery_protection_token] ||
  form_authenticity_token ==
    request.headers['X-CSRF-Token']
end
```

The second line short-circuits the CSRF check: it means that if `request.get?` is `true`, the request is considered "verified" and the CSRF check is skipped. In fact, in the Rails source there is a comment above this method that says:

> Gets should be safe and idempotent.

In your application, you may always use `POST` to make requests to `/products/:id/purchase`. But because the router allows `GET` requests as well, an attacker can trivially bypass the CSRF protection for any method routed via the `#match` helper. If your application uses the old wildcard route (not recommended), the CSRF protection is completely ineffective.

**Best Practice:** Don't use `GET` for unsafe actions. Don't use `#match` to add routes (instead use `#post`, `#put`, etc.). Ensure you don't have wildcard routes.

**The Fix:** Rails now requires you to specify either specific HTTP verbs or `via: :all` when adding routes with `#match`. The generated `config/routes.rb` no longer contains commented out `#match` routes. (The wildcard route is also removed.)

[]{#format-anchors}

### 2. Regular Expression Anchors in Format Validations

Consider the following validation:

``` {.highlight .ruby}
validates_format_of :name, with: /^[a-z ]+$/i
```

This code is usually a subtle bug. The developer probably meant to enforce that the entire name attribute is composed of only letters and spaces. Instead, this will only enforce that at least one line in the name is composed of letters and spaces. Some examples of regular expression matching make it more clear:

``` {.highlight .ruby}
>> /^[a-z ]+$/i =~ "Joe User"
=> 0 # Match

>> /^[a-z ]+$/i =~ " '); -- foo"
=> nil # No match

>> /^[a-z ]+$/i =~ "a\n '); -- foo"
=> 0 # Match
```

The developer should have used the `\A` (beginning of string) and `\z` (end of string) anchors instead of `^` (beginning of line) and `$` (end of line). The correct code would be:

``` {.highlight .ruby}
validates_format_of :name, with: /\A[a-z ]+\z/i
```

You could argue that the developer is at fault, and you'd be right. However, the behavior of regular expression anchors is not necessarily obvious, especially to developers who are not considering multiline values. (Perhaps the attribute is only exposed in a text input field, never a `textarea`.)

Rails is at the right place in the stack to save developers from themselves and that's exactly what has been done in Rails 4.

**Best Practice:** Whenver possible, use `\A` and `\z` to anchor regular expressions instead of `^` and `$`.

**The Fix:** Rails 4 introduces a `multiline` option for `validates_format_of`. If your regular expression is anchored using `^` and `$`rather than `\A` and `\z` and you do not pass `multiline: true`, Rails will raise an exception. This is a great example of creating safer default behavior, while still providing control to override it where necessary.

[]{#clickjacking}

### 3. Clickjacking

Clickjacking or "UI redress attacks" involve rendering the target site in an invisible frame, and tricking a victim to take an unexpected action when they click. If a site is vulnerable to clickjacking, an attacker may trick users into taking undesired actions like making a one-click purchase, following someone on Twitter, or changing their privacy settings.

To defend against clickjacking attacks, a site must prevent itself from being rendered in a `frame` or `iframe` on sites that it does not control. Older browsers required ugly "frame busting" JavaScripts, but modern browsers support the [`X-Frame-Options` HTTP header](https://developer.mozilla.org/en-US/docs/HTTP/X-Frame-Options) which instructs the browser about whether or not it should allow the site to be framed. This header is easy to include, and not likely to break most websites, so Rails should include it by default.

**Best Practice:** Use the [secure\_headers](https://github.com/twitter/secureheaders) RubyGem by Twitter to add an `X-Frame-Options` header with the value of `SAMEORIGIN` or `DENY`.

**The Fix:** By default, Rails 4 now sends the `X-Frame-Options` header with the value of `SAMEORIGIN`:

``` {.highlight .plaintext}
X-Frame-Options: SAMEORIGIN
```

This tells the browser that your application can only be framed by pages originating from the same domain.

[]{#readable-sessions}

### 4. User-Readable Sessions

The default Rails 3 session store uses signed, unencrypted cookies. While this protects the session from tampering, it is trivial for an attacker to decode the contents of a session cookie:

``` {.highlight .ruby}
session_cookie = <<-STR.strip.gsub(/\n/, '')
BAh7CEkiD3Nlc3Npb25faWQGOgZFRkkiJTkwYThmZmQ3Zm
dAY7AEZJIgtzZWtyaXQGOâ¦--4c50026d340abf222â¦
STR

Marshal.load(Base64.decode64(session_cookie.split("--")[0]))
# => {
#   "session_id"  => "90a8f...",
#   "_csrf_token" => "iUoXA...",
#   "secret"      => "sekrit"
# }
```

It's unsafe to store any sensitive information in the session. Hopefully this is a well known, but even if a user's session does not contain sensitive data, it can still create risk. By decoding the session data, an attacker can gain useful information about the internals of the application that can be leveraged in an attack. For example, it may be possible to understand which authentication system is in use (Authlogic, Devise, etc.).

While this does not create a vulnerability on its own, it can aid attackers. Any information about how the application works can be used to hone exploits, and in some cases to avoid triggering exceptions or tripwires that could give the developer an early warning an attack is underway.

User-readable sessions violate the Principle of Least Privilege, because even though the session data must be passed to the visitor's browser, the visitor does not need to be able to read the data.

**Best Practice:** Don't put any information into the session that you wouldn't want an attacker to have access to.

**The Fix:** Rails 4 changed the default session store to be encrypted. Users can no longer decode the contents of the session without the decryption key, which is not available on the client side.

Unresolved Issues
-----------------

The remainder of this post covers security risks that are still present in Rails' at the time of publication. Hopefully, at least some of these will be fixed, and I will update this post if that is the case.

[]{#server-header}

### 1. Verbose `Server` Headers

The default Rails server is WEBrick (part of the Ruby standard library), even though it is rare to run WEBrick in production. By default, WEBrick returns a verbose `Server` header with every HTTP response:

``` {.highlight .plaintext}
HTTP/1.1 200 OK
# â¦
Server: WEBrick/1.3.1 (Ruby/1.9.3/2012-04-20)
```

Looking at the WEBrick source, you can see the header is composed with a few key pieces of information:

``` {.highlight .ruby}
"WEBrick/#{WEBrick::VERSION} " +
"(Ruby/#{RUBY_VERSION}/#{RUBY_RELEASE_DATE})",
```

This exposes the WEBrick version, and also the specific Ruby patchlevel being run (since release dates map to patchlevels). With this information, spray and prey scanners can target your server more effectively, and attackers can tailor their attack payloads.

**Best Practice:** Avoid running WEBrick in production. There are better servers out there like Passenger, Unicorn, Thin and Puma.

**The Fix:** While this issue originates in the WEBrick source, Rails should configure WEBrick to use a less verbose `Server` header. Simply "Ruby" seems like a good choice.

[]{#server-binding}

### 2. Binding to 0.0.0.0

If you boot a Rails server, you'll see something like this:

``` {.highlight .plaintext}
$ ./script/rails server -e production
=> Booting WEBrick
=> Rails 3.2.12 application starting in production on http://0.0.0.0:3000
```

Rails is binding on 0.0.0.0 (all network interfaces) instead of 127.0.0.1 (local interface only). This can create security risk in both development and production contexts.

In development mode, Rails is not as secure (for example, it renders diagnostic 500 pages). Additionally, developers may load a mix of production data and testing data (e.g. username: admin / password: admin). Scanning for web servers on port 3000 in a San Francisco coffee shop would probably yield good targets.

In production, Rails should be run behind a proxy. Without a proxy, IP spoofing attacks are trivial. But if Rails binds on 0.0.0.0, it may be possible to easily circumvent a proxy by hitting Rails directly depending on the deployment configuration.

Therefore, binding to 127.0.0.1 is a safer default than 0.0.0.0 in all Rails environments.

**Best Practice:** Ensure your Web server process is binding on the minimal set of interfaces in production. Avoid loading production data on your laptop for debugging purposes. If you must do so, load a minimal dataset and remove it as soon as it's no longer necessary.

**The Fix:** Rails already provides a `--binding` option to change the IP address that the server listens on. The default should be changed from 0.0.0.0 to 127.0.0.1. Developers who need to bind to other interfaces in production can make that change in their deployment configurations.

[]{#versioned-secrets}

### 3. Versioned Secret Tokens

Every Rails app gets a long, randomly-generated secret token in `config/initializers/secret_token.rb` when it is created with `rails new`. It looks something like this:

``` {.highlight .ruby}
WebStore::Application.config.secret_token = '4f06a7aâ¦72489780f'
```

Since Rails creates this automatically, most developers do not think about it much. But this secret token is like a root key for your application. If you have the secret token, it is trivial to forge sessions and escalate privileges. It is one of the most critical pieces of sensitive data to protect. Encryption is only as good as your key management practices.

Unfortunately, Rails falls flat in dealing with these secret token. The `secret_token.rb` file ends up checked into version control, and copied to GitHub, CI servers and every developer's laptop.

**Best Practice:** Use a different secret token in each environment. Inject it via an ENV var into the application. As an alternative, symlink the production secret token in during deployment.

**This Fix:** At a minimum, Rails should `.gitignore` the `config/initializers/secret_token.rb` file by default. Developers can symlink a production token in place when they deploy or change the initializer to use an ENV var (on e.g. Heroku).

I would go further and propose that Rails create a storage mechanism for secrets. There are many libraries that provide installation instructions involving checking secrets into initializers, which is a bad practice. At the same time, there are at least two popular strategies for dealing with this issue: ENV vars and symlinked initializers.

Rails is in the right place to provide a simple API that developers can depend on for managing secrets, with a swappable backend (like the cache store and session store).

[]{#logging-sql}

### 4. Logging Values in SQL Statements

The `config.filter_parameters` Rails provides is a useful way to prevent sensitive information like passwords from accumulating in production log files. But it does not affect logging of values in SQL statements:

``` {.highlight .plaintext}
Started POST "/users" for 127.0.0.1 at 2013-03-12 14:26:28 -0400
Processing by UsersController#create as HTML
  Parameters: {"utf8"=>"âÅâ", "authenticity_token"=>"...",
  "user"=>{"name"=>"Name", "password"=>"[FILTERED]"}, "commit"=>"Create User"}
  SQL (7.2ms)  INSERT INTO "users" ("created_at", "name", "password_digest",
  "updated_at") VALUES (?, ?, ?, ?)  [["created_at",
  Tue, 12 Mar 2013 18:26:28 UTC +00:00], ["name", "Name"], ["password_digest",
  "$2a$10$r/XGSY9zJr62IpedC1m4Jes8slRRNn8tkikn5.0kE2izKNMlPsqvC"], ["updated_at",
  Tue, 12 Mar 2013 18:26:28 UTC +00:00]]
Completed 302 Found in 91ms (ActiveRecord: 8.8ms)
```

The default Rails logging level in production mode (info) will not log SQL statements. The risk here is that sometimes developers will temporarily increase the logging level in production when debugging. During those periods, the application may write sensitive data to log files, which then persist on the server for a long time. An attacker who gains access to read files on the server could find the data with a simple `grep`.

**Best Practice:** Be aware of what is being logged at your production log level. If you increase the log level temporarily, causing sensitive data to be logged, remove that data as soon as it's no longer needed.

**The Fix:** Rails could change the `config.filter_parameters` option into something like `config.filter_logs`, and apply it to both parameters and SQL statements. It may not be possible to properly filter SQL statements in all cases (as it would require a SQL parser) but there may be an 80/20 solution that could work for standard inserts and updates.

As an alternative, Rails could redact the entire SQL statement if it contains references to the filtered values (for example, redact all statements containing "password"), at least in production mode.

[]{#offsite-redirects}

### 5. Offsite Redirects

Many applications contain a controller action that needs to send users to a different location depending on the context. The most common example is a `SessionsController` that directs the newly authenticated user to their intended destination or a default destination:

``` {.highlight .ruby}
class SignupsController < ApplicationController
  def create
    # ...
    if params[:destination].present?
      redirect_to params[:destination]
    else
      redirect_to dashboard_path
    end
  end
end
```

This creates the risk that an attacker can construct a URL that will cause an unsuspecting user to be sent to a malicious site after they login:

``` {.highlight .plaintext}
https://example.com/sessions/new?destination=http://evil.com/
```

Unvalidated redirects can be used for phishing or may damage the users trust in you because it appears that you sent them to a malicious website. Even a vigilant user may not check the URL bar to ensure they are not being phished after their first page load. The issue is serious enough that it has made it into the latest edition of the OWASP Top Ten Application Security Threats.

**Best Practice:** When passing a hash to `#redirect_to`, use the `only_path: true` option to limit the redirect to the current host:

``` {.highlight .ruby}
redirect_to params.merge(only_path: true)
```

When passing a string, you can parse it an extract the path:

``` {.highlight .ruby}
redirect_to URI.parse(params[:destination]).path
```

**The Fix:** By default, Rails should only allow redirects within the same domain (or a whitelist). For the rare cases where external redirects are intended, the developer should be required to pass an `external: true` option to `redirect_to` in order to opt-in to the more risky behavior.

[]{#linkto-xss}

### 6. Cross Site Scripting (XSS) Via `link_to`

Many developers don't realize that the HREF attribute of the `link_to` helper can be used to inject JavaScript. Here is an example of unsafe code:

``` {.highlight .erb}
<%= link_to "Homepage", user.homepage_url %>
```

Assuming the user can set the value of their `homepage_url` by updating their profile, it creates the risk of XSS. This value:

``` {.highlight .ruby}
user.homepage_url = "javascript:alert('hello')"
```

Will generate this HTML:

``` {.highlight .html}
<a href="javascript:alert('hello')">Homepage</a>
```

Clicking the link will execute the script provided by the attacker. Rails' XSS protection will not prevent this. This used to be necessary and common before the community migrated to more unobtrusive JavaScript techniques, but is now a vestigial weakness.

**Best Practice:** Avoid using untrusted input in HREFs. When you must allow the user to control the HREF, run the input through `URI.parse` first and sanity check the protocol and host.

**The Fix:** Rails should only allow paths, HTTP, HTTPS and `mailto:` href values in the `link_to` helper by default. Developers should have to opt-in to unsafe behavior by passing in an option to the `link_to` helper, or `link_to` could simply not support this and developers can craft their links by hand.

[]{#sqli}

### 7. SQL Injection

Rails does a relatively good job of preventing common SQL injection (SQLi) attacks, so developers may think that Rails is immune to SQLi. Of course, that is not the case. Suppose a developer needs to pull either subtotals or totals off the `orders` table, based on a parameter. They might write:

``` {.highlight .ruby}
Order.pluck(params[:column])
```

This is not a safe thing to do. Clearly, the user can now manipulate the application to retrieve any column of data from the `orders` table that they wish. What is less obvious, however, is that the attacker can also pull values from other tables. For example:

``` {.highlight .ruby}
params[:column] = "password FROM users--"
Order.pluck(params[:column])
```

Will become:

``` {.highlight .sql}
SELECT password FROM users-- FROM "orders"
```

Similarly, the `column_name` attribute to `#calculate` actually accepts arbitrary SQL:

``` {.highlight .ruby}
params[:column] = "age) FROM users WHERE name = 'Bob'; --"
Order.calculate(:sum, params[:column])
```

Will become:

``` {.highlight .sql}
SELECT SUM(age) FROM users WHERE name = 'Bob'; --) AS sum_id FROM "orders"
```

Controlling the `column_name` attribute of the `#calculate` method allows the attacker to pull specific values from arbitrary columns on arbitrary tables.

[Rails-SQLi.org](http://rails-sqli.org) details which ActiveRecord methods and options permit SQL, with examples of how they might be attacked.

**Best Practice:** Understand the APIs you use and where they might permit more dangerous operations than you'd expect. Use the safest APIs possible, and whitelist expected inputs.

**The Fix:** This one is difficult to solve en masse, as the proper solution varies by context. In general, ActiveRecord APIs should only permit SQL fragments where they are commonly used. Method parameters named `column_name` should only accept column names. Alternative APIs can be provided for developers who need more control.

Hat tip to Justin Collins of Twitter for writing [rails-sqli.org](http://rails-sqli.org) which made me aware of this issue.

[]{#yaml}

### 8. YAML Deserialization

As many Ruby developers learned in January, deserializing untrusted data with YAML is as unsafe as `eval`. There's been a lot written about YAML-based attacks, so I won't rehash it here, but in summary if the attacker can inject a YAML payload, they can execute arbitrary code on the server. The application does not need to do anything other than load the YAML in order to be vulnerable.

Although Rails was patched to avoid parsing YAML sent to the server in HTTP requests, it still uses YAML as the default serialization format for the `#serialize` feature, as well as the new `#store` feature (which is itself a thin wrapper around `#serialize`). Risky code looks like this:

``` {.highlight .ruby}
class User < ActiveRecord::Base
  # ...
  serialize :preferences

  store :theme, accessors: [ :color, :bgcolor ]
end
```

Most Rails developers would not feel comfortable with storing arbitrary Ruby code in their database, and `eval`ing it when the records are loaded, but that's the functional equivalent of using YAML deserialization in this way. It violates the Principle of Least Privilege when the stored data does not include arbitrary Ruby objects. Suddenly a vulnerability allowing the writing of a value in a database can be springboarded into taking control of the entire server.

The use of YAML is especially concerning to me as it looks safe but is dangerous. The YAML format was looked at for years by hundreds of skilled developers before the remote code execution (RCE) vulnerability was exposed. While this is top of mind in the Ruby community now, new developers who pick up Rails next year will not have experienced the YAML RCE fiasco.

**Best Practice:** Use the JSON serialization format instead of YAML for `#serialize` and `#store`:

``` {.highlight .ruby}
class User < ActiveRecord::Base
  serialize :preferences, JSON
  store :theme, accessors: [ :color, :bgcolor ], coder: JSON
end
```

**The Fix:** Rails should switch its default serialization format for ActiveRecord from YAML to JSON. The YAML behavior should be either available by opt-in or extracted into an optional Gem.

[]{#mass-assignment}

### 9. Mass Assignment

Rails 4 switched from using `attr_accessible` to deal with mass assignment vulnerabilities to the strongparameters approach. The `params` object is now an instance of `ActionController::Parameters`. strongparameters works by checking that instances of `Parameters` used in mass assignment are "permitted" -- that a developer has specifically indicated which keys (and value types) are expected.

In general, this is a positive change, but it does introduce a new attack vector that was not present in the `attr_accessible` world. Consider this example:

``` {.highlight .ruby}
params = { user: { admin: true }.to_json }
# => {:user=>"{\"admin\":true}"}

@user = User.new(JSON.parse(params[:user]))
```

`JSON.parse` returns an ordinary Ruby `Hash` rather than an instance of `ActionController::Parameters`. With strong\_parameters, the default behavior is to allow instances of `Hash` to set any model attribute via mass assignment. The same issue occurs if you use `params` from a Sinatra app when accessing an ActiveRecord model -- Sinatra will not wrap the Hash in an instance of `ActionController::Parameters`.

**Best Practice:** Rely on Rails' out-of-the-box parsing whenever possible When combining ActiveRecord models with other web frameworks (or deserializing data from caches, queues, etc.) wrap input in `ActionController::Parameters` so that strong\_parameters works.

**The Fix:** It's unclear what the best way for Rails to deal with this is. Rails could override deserialization methods like `JSON.parse` to return instances of `ActionController::Parameters` but that is relatively invasive and could cause compatibility issues.

A concerned developer could combine strongparameters with \`attraccessible`for highly sensitive fields (like`User\#admin\`) for extra protection, but that is likely overkill for most situations. In the end, this may just be a behavior we need to be aware of and look out for.

**Update:** If you've made it all the way here and want to learn more about Rails security, check out our [free, 1-month Rails security email course](http://railssecurity.com/).

Hat tip to Brendon Murphy for making me aware of this issue.

Thanks to Adam Baldwin, Justin Collins, Neil Matatell, Noah Davis and Aaron Patterson for reviewing this article.
