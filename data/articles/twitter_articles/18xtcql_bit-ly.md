---
title: "Feds Are Suspects in New Malware That Attacks Tor Anonymity"
url: http://bit.ly/18XTcql
keywords: hosting,malware,suspects,feds,anonymity,firefox,ip,virginia,attacks,hidden,browser,fbi,tor,code
---
Security researchers tonight are poring over a piece of malicious software that takes advantage of a Firefox security vulnerability to identify some users of the privacy-protecting Tor anonymity network.

The malware showed up Sunday morning on multiple websites hosted by the anonymous hosting company Freedom Hosting. That would normally be considered a blatantly criminal "drive-by" hack attack, but nobody's calling in the FBI this time. The FBI is the prime suspect.

"It just sends identifying information to some IP in Reston, Virginia," says reverse-engineer Vlad Tsyrklevich. "It's pretty clear that it\'s FBI or it\'s some other law enforcement agency that's U.S.-based."

If Tsrklevich and other researchers are right, the code is likely the first sample captured in the wild of the FBI's \"computer and internet protocol address verifier,\" or CIPAV, the law enforcement spyware first [reported](https://www.wired.com/politics/law/news/2007/07/fbi_spyware) by WIRED in 2007.

Court documents and FBI files released under the FOIA have described the CIPAV as software the FBI can deliver through a browser exploit to gather information from the target's machine and send it to an FBI server in Virginia. The FBI has [been using the CIPAV](https://www.wired.com/threatlevel/2009/04/fbi-spyware-pro/) since 2002 against hackers, online sexual predators, extortionists, and others, primarily to identify suspects who are disguising their location using proxy servers or anonymity services, like Tor.

The code has been used sparingly in the past, which kept it from leaking out and being analyzed or added to anti-virus databases.

The broad Freedom Hosting deployment of the malware coincides with the [arrest of Eric Eoin Marques](http://www.independent.ie/irish-news/courts/fbi-bids-to-extradite-largest-childporn-dealer-on-planet-29469402.html) in Ireland on Thursday on an U.S. extradition request. The Irish Independent reports that Marques is wanted for distributing child pornography in a federal case filed in Maryland, and quotes an FBI special agent describing Marques as \"the largest facilitator of child porn on the planet.\"

Freedom Hosting has long been notorious for allowing child porn to live on its servers. In 2011, the hactivist collective Anonymous [singled out](http://pastebin.com/T1LHnzEW) Freedom Hosting for denial-of-service attacks after allegedly finding the firm hosted 95 percent of the child porn hidden services on the Tor network.

Freedom Hosting is a provider of turnkey "Tor hidden service" sites -- special sites, with addresses ending in .onion -- that hide their geographic location behind layers of routing, and can be reached only over the Tor anonymity network.

Tor hidden services are ideal for websites that need to evade surveillance or protect users\' privacy to an extraordinary degree -- which can include human rights groups and journalists. But it also naturally appeals to serious criminal elements.

Shortly after Marques' arrest last week, all of the hidden service sites hosted by Freedom Hosting began displaying a "Down for Maintenance" message. That included websites that had nothing to do with child pornography, such as the secure email provider TorMail.

Some visitors looking at the source code of the maintenance page realized that it included a hidden `iframe` tag that loaded a mysterious clump of Javascript code from a Verizon Business internet address located in Virginia.

By midday Sunday, the code was being circulated and dissected all over the net. Mozilla confirmed the code exploits a critical memory management vulnerability in Firefox that was [publicly reported](http://www.mozilla.org/security/announce/2013/mfsa2013-53.html) on June 25, and is fixed in the latest version of the browser.

Though many older revisions of Firefox are vulnerable to that bug, the malware only targets Firefox 17 ESR, the version of Firefox that forms the basis of the Tor Browser Bundle -- the easiest, most user-friendly package for using the Tor anonymity network.

"The malware payload could be trying to exploit potential bugs in Firefox 17 ESR, on which our Tor Browser is based," the [non-profit Tor Project](https://blog.torproject.org/blog/hidden-services-current-events-and-freedom-hosting) wrote in a blog post Sunday. "We\'re investigating these bugs and will fix them if we can."

The inevitable conclusion is that the malware is designed specifically to attack the Tor browser. The strongest clue that the culprit is the FBI, beyond the circumstantial timing of Marques' arrest, is that the malware does nothing but identify the target.

The payload for the Tor Browser Bundle malware is hidden in a variable called \"magneto\".

The heart of the malicious Javascript is a tiny Windows executable hidden in a variable named "Magneto." A traditional virus would use that executable to download and install a full-featured backdoor, so the hacker could come in later and steal passwords, enlist the computer in a DDoS botnet, and generally do all the other nasty things that happen to a hacked Windows box.

But the Magneto code doesn't download anything. It looks up the victim's MAC address -- a unique hardware identifier for the computer's network or Wi-Fi card -- and the victim\'s Windows hostname. Then it sends it to the Virginia server, outside of Tor, to expose the user\'s real IP address, and coded as a standard HTTP web request.

"The attackers spent a reasonable amount of time writing a reliable exploit, and a fairly customized payload, and it doesn't allow them to download a backdoor or conduct any secondary activity," says [Tsyrklevich, who reverse-engineered the Magneto code](http://tsyrklevich.net/tbb_payload.txt).

The malware also sends, at the same time, a serial number that likely ties the target to his or her visit to the hacked Freedom Hosting-hosted website.

In short, Magneto reads like the x86 machine code embodiment of a carefully crafted court order authorizing an agency to blindly trespass into the personal computers of a large number of people, but for the limited purpose of identifying them.

But plenty of questions remain. For one, now that there\'s a sample of the code, will anti-virus companies start detecting it?

**Update 8.5.13 12:50:** According to Domaintools, the malware\'s command-and-control IP address in Virginia is [allocated to Science Applications International Corporation](http://www.domaintools.com/research/ip-explorer/?ip=65.222.202.54). Based in McLean, Virginia, SAIC is a major technology contractor for defense and intelligence agencies, including the FBI. I have a call in to the firm.

**13:50** Tor Browser Bundle users who installed or manually updated after June 26 are safe from the exploit, according to the Tor Project\'s new [security advisory](https://blog.torproject.org/blog/tor-security-advisory-old-tor-browser-bundles-vulnerable) on the hack.

**14:30:** SAIC has no comment.

**15:10:** There are incorrect press reports circulating that the command-and-control IP address belongs to the NSA. Those reports are based on a misreading of domain name resolution records. The NSA\'s public website, NSA.gov, is served by the same upstream Verizon network as the Tor malware command-and-control server, but that network handles tons of [government agencies and contractors](http://cryptome.org/eyeball/verizon-spy2/verizon-spy2.htm) in the Washington DC area.

**8.6.13 17:10:** SAIC\'s link to the IP addresses may be an error in Domaintools\' records. The official IP allocation records maintained by the [American Registry for Internet Numbers](https://www.arin.net/) show the two Magneto-related addresses are not part of SAIC\'s publicly-listed allocation. They\'re part of a ghost block of eight IP addresses that have no organization listed. Those addresses trace no further than the Verizon Business data center in Ashburn, Virginia, 20 miles northwest of the Capital Beltway. (Hat tip: [Michael Tigas](https://gist.github.com/mtigas/6158214))
