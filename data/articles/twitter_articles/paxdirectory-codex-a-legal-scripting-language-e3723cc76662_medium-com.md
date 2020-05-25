---
title: "Codex: A Legal Scripting Language for Ethereum"
url: https://medium.com/@PaxDirectory/codex-a-legal-scripting-language-e3723cc76662#.450i93o9o
keywords: way,example,users,ethereum,contracts,contract,codex,statement,legal,language,statements,scripting
---
Codex: A Legal Scripting Language for Ethereum {#eb58 .graf .graf--h3 .graf--leading .graf--title name="eb58"}
==============================================

[![Go to the profile of Pax](https://cdn-images-1.medium.com/fit/c/100/100/1*3Js8FxkgG5NGNDjEQkNSmA.jpeg){.avatar-image .u-size50x50}](https://medium.com/@PaxDirectory?source=post_header_lockup){.link .u-baseColor--link .avatar}[Pax](https://medium.com/@PaxDirectory){.ds-link .ds-link--styleSubtle .ui-captionStrong .u-inlineBlock .link .link--darken .link--darker}

Feb 24, 2016

![](https://cdn-images-1.medium.com/freeze/max/60/1*OY_XchVkmvbYWhWeBPRFwQ.jpeg?q=20){.progressiveMedia-thumbnail .js-progressiveMedia-thumbnail}![](https://cdn-images-1.medium.com/max/1600/1*OY_XchVkmvbYWhWeBPRFwQ.jpeg){.progressiveMedia-noscript .js-progressiveMedia-inner}

Pax is using Ethereum to build a peer to peer legal system. The best way to explain Ethereum is by contrasting it with Bitcoin. What Bitcoin is to money, Ethereum is (potentially) to law. Bitcoin's value comes from the fact that every transaction that happens is added to the record and can't be changed. Each full node on the network holds a complete copy of the transaction history, which eliminates any possibility of double-spending. It turns out that this approach can also be used to create binding self-enforcing legal contracts between people, which can have use cases as wide ranging as employment, rent, deeds, property transfer, restitution, incorporation, subscriptions, billing, voting and dividend systems. Where there are disputes, a blockchain can hold an objective record of events making dispute resolution relatively trivial compared to traditional legal systems, both on the back-end (legislation) and the front-end (arbitration).

Codex is a legal scripting DSL (domain specific language) geared towards creating executable contracts via the Pax directory and API. Codex is a flexible and powerful way for clients to interact with Ethereum, and is underwritten by Solidity (one of Ethereum's most popular high-level programming languages) and the Web3.js, which is a Javascript library which allows front-facing apps to connect to the Ethereum network.

#### Contract Types {#3688 .graf .graf--h4 .graf-after--p name="3688"}

We can distinguish four basic genres of legal contract: didactic contracts, social contracts, smart contracts and executable contracts. Of these four genres, there are two basic types: sovereign and polycentric.

Jurisdictions that are enforced by a nation state are sovereign. Jurisdictions that occur through voluntary consent (with exit rights) are considered polycentric.

**DIDACTIC CONTRACTS** (sovereign, low-trust) are what most people are familiar with- "Terms and Conditions". Authority for enforcement comes from common law and government statute books. Written in defensive legalese (low trust), mapping out in detail every aspect of human behaviour involved in the agreement. Since traditional didactic contracts are mostly unread, they do not in most cases involve active consent, which has moral hazard.

**SOCIAL CONTRACTS** (sovereign, high-trust) is the basis of the authority of sovereign territorial monopolies. Essentially theological in nature, unwritten, undefined, unconsented to. Institutionally epitomized by a Head of State, or "Leviathan".

**SMART CONTRACTS** (polycentric, low-trust) are small computer programs (or "bots") which exist on a distributed ledger which can always be relied upon to execute their encoded instructions. Because of the nature of blockchain architecture, they are trustless: there is no intermediary other than the network itself. Ethereum is the leading platform for writing and hosting smart contracts on the blockchain.

**EXECUTABLE CONTRACTS** (polycentric, high-trust) are immediately applicable within a voluntary, high-trust environment which can be created using a social networking interface with identity and reputation. Executable contracts call smart contract functions for different purposes and are simple, human-readable and digitally signed by the parties involved. They can also define and deploy payment logic and consequences according to the defined conditionals. Codex is a language for writing executable contracts and Pax is the high trust environment in which these contracts occur.

There will be two ways that users can build contracts: a block-dropper and a terminal. The block-dropper allows users in an environment similar to a Messenger app to drop blocks that have some kind of logical relationship, which describe in plain English what they user wants them to do. Then for more advanced users, there is the option of a terminal where they can enter the Codex code. In the long run there will also be an API available so that all this can be done remotely, and incorporate contracts dynamically into services.

The following section will discuss the specification for Codex.

![](https://cdn-images-1.medium.com/freeze/max/60/1*3fcWQm67aG2SUtwnOarrjw.png?q=20){.progressiveMedia-thumbnail .js-progressiveMedia-thumbnail}![](https://cdn-images-1.medium.com/max/1600/1*3fcWQm67aG2SUtwnOarrjw.png){.progressiveMedia-noscript .js-progressiveMedia-inner}

#### Member Keywords {#d28c .graf .graf--h4 .graf-after--figure name="d28c"}

There are three kinds of contracts: BILATERAL, MULTILATERAL and UNILATERAL.

**with** contracts are bilateral (one to one), from the contract's initiator to an individual subject. The subject is named after the with statement. In the Codex terminal, this keyword is detected and there is the option to insert either a raw Ethereum ID or the supplied name or handle of the subject's identity within the directory.

> with subject:

**between** contracts are multilateral (many to many), and involve multiple subjects- "Multisig" in Bitcoin terminology. **between** contracts can specify a diversity of clauses and relationships between the subjects of the contract. A "roll" is a list of subjects to whom a contract applies.

> between roll\[subjects\]:

**for** contracts are unilateral (one to many). A unilateral contract is between one initiator and multiple subjects. **for** contracts take a roll (i.e. list of allies from the directory), as an argument. Whenever a client is added to the roll, a new instantiation of the contract commences between the initiator and the subject from the moment the new member stamps the contract to confirm consent.

> for roll\[subjects\]:

The **roll** keyword invokes an array of allies. Just like allies are pre-connected on the directory before contracts can happen, rolls are also pre-created before they can be invoked at the beginning of a contract. If an ally is added to a roll which is already inserted into a live "for contract", another iteration of that contract begins from then on.

![](https://cdn-images-1.medium.com/freeze/max/60/1*zhGAS3jc16YZdrI5o399qg.png?q=20){.progressiveMedia-thumbnail .js-progressiveMedia-thumbnail}![](https://cdn-images-1.medium.com/max/1600/1*zhGAS3jc16YZdrI5o399qg.png){.progressiveMedia-noscript .js-progressiveMedia-inner}

#### Temporal Keywords {#b02b .graf .graf--h4 .graf-after--figure name="b02b"}

In Codex there are two kinds of events in time: SINGULAR and INTERVAL events. Future dates take the form of (t + x) where x is an integer which represents daily intervals from t, the present. (t + 1) is tomorrow, or more precisely, one day after t is triggered. (t + 7) is a week after t. (t + 200) is 200 days after t. And so on. You can use division to represent units of time smaller than one day: (t + 1/24) is one hour after t.

**on** statements specify a singular temporal event in the logic of a clause. This is a simple contract where you send your friend Bob a birthday gift of 100 credits in 12 days time (although making a contract with him might spoil the surprise somewhat!):

> with Bob:

> pay 100 on(t + 12).

**every** statements specify a repeating interval in the logic of a clause. A good example of contracts which would use **every** statements would be employment contracts, rent agreements, loan contracts, subscriptions and bills. This is a very simple employment contract where all the workers on the same salary level would get paid 600 credits on a weekly basis (real world employment contracts would be much more complicated and contain conditionals, but we'll get to that later):

> for roll\[workers\]:

> pay 500 every(t + 7).

Here is a simple bilateral rent contract. 365/12 represents a monthly interval- since months have different numbers of days this is the best way to express a repeating monthly payment.

> with landlord:

> pay 800 every(t + 365/12).

**start** and **stop** statements indicate the beginning or end of an event. For example if a magazine had a unilateral contract with subscribers to subscribe to the magazine for 12 months at 10 credits per month, after a one month free trial, you could write a contract like this:

> for roll\[subscribers\]:

> take 10 every(t + 365/12),

> start(t + 365/12),

> stop(t + 365).

**Conditional Keywords**

Legal contracts in the real world don't simply define payment or event logic, they set rules for human behaviour within certain contexts. The traditional legal approach was to set out these behaviours in excruciating legal detail. But this doesn't make sense; in many contracts (especially "terms and conditions") it is impractical to expect that users will have the time or legal discernment to examine every detail of what they are signing up to.

These defensive measures exist to protect firms from expensive litigation in nation state court systems which are built on this model. But the model does not make logical sense in reality. "Tickbox consent" is impractical and coercive, in that the initiator may use it to enforce terms that were not cognitively agreed to. Under Pax, it is consent which is the source of a contract's legitimacy, and is the authority of its proportionate enforcement. A Codex contract will allow legal plaintext to be entered into the contract, as conditionals, which can be dynamically completed from within the user's account admin; and when a contract is stamped by the initiator, a digest is produced to which summarizes the terms in a compact manner so that the subject is aware.

**if** statements signify a conditional, both in event logic and in behavioural adherence to the content of legal plaintext. Here is an example of a contract between a firm and a consultant to write a report (with an open-ended timeline in the contract, though an estimate probably agreed verbally) where it is agreed that half will be paid now and half on completion of the project. Furthermore, there will be a 25% bonus for the consultant if the report is approved by a committee.

> with consultant:

> pay 2000,

> if(do\[1\]: "Evaluate the whole project and write a report."

> do\[2\]: "The recommendations get approved by the committee." ):

> pay 2000 on(t + do\[1\]),

> pay 1000 on(t + do\[2\]),

> else: exit.

**do** statements are followed by an item of user defined plaintext, with a length limit of a certain number of bytes as yet to be decided, which represents a sort of verbal agreement. If there are multiple **do** statements, they are numbered with square brackets. In the inventory screen of each client, a do statement will appear as an item in the live contract to be ticked off. This must then be confirmed by both sides of the contract- in the above case to trigger the second half-payment, and finally the 25% bonus.

**else** statements on their own are a way to define an open-ended deviation from a conditional. In the above contract, if the consultant does not fulfil the**do** obligations, the contractor can tick "no", which will trigger a termination of the contract. In the above case, the contractor would keep their deposit but would not get paid the sum of their contract.

**not, and, or** statements operate on **do** in several ways. **do not** obviously represents a statement forbidding a certain action. Where else represents an open-ended deviation from the defined conditionals, **do not** specifies particular actions which would trigger a consequence. Here, for example is a non-disclosure agreement between a worried screenwriter who is paying a copyeditor to proofread the script within a week (the screenwriter is initiating). They agree on a fee of 800, and as insurance if the copyeditor tells anyone about the script the fee will be reversed, creating an incentive for secrecy until the film is release in two years time.

> with copyeditor:

> if(do not:

> "Divulge the plot or tell anyone about the script."):

> pay 800 on(t + 7),

> else: take 1600 on(t + do),

> exit(t + 730).

Let's take a closer look at this contract. When there is only one **do**statement, it does not need to be tagged with a number. That is why in the**else** line, the statement features **do** which tags the **do not** conditional (**not**merely negates the **do**). So if the condition is ever violated, the conditional can be triggered at any time to take back double the original fee (harsh!). As is true with any scripting language, there are always multiple ways of going about the same thing, and different people will have different preferences. For example, this could be phrased as a positive **do** conditional of "Keep the plot secret"... or **else**. At the end of the contract there is an **exit** statement which governs the timeframe over which the contract is valid (one assumes, until the film is released to the public). After **t + 730** days, the contract exits, and a receipt of the contract is produced and filed to Ethereum.

**and, or** statements also operate on **do** conditionals, by allow multiple physically unrelated conditional statements to be chained together in a way that is contingent on one particular consequence being executed by the contract. In real life, contracts will contain a diversity of conditionals all of which taken together may only trigger one consequence.

#### Consequential Keywords {#7a21 .graf .graf--h4 .graf-after--p name="7a21"}

pay and take statements initiate a payment at the appointed time, depending on who is initiating the contract (especially in two-way with and for contracts). If the funds in the user account are insufficient, the default action is to cancel the contract and produce a receipt. Alternatively, it could be possible to write a further conditional using the negation "!" syntax, which defines what to do in case the pay function fails. This could be to try again in a week (as in a direct debit) or send a text message.

A realistic tenancy agreement would be a lot more complex and have various other clauses and do statements than the short example given earlier, but pay and take statements are the simplest consequential. Because Codex is essentially an arrangement of function calls on pre-written Ethereum smart contract, it is possible to continually top up the required amount of credits in advance of the transaction as per the contract. This is less easy when writing new Solidity contracts from scratch. The directory takes care of everything else.

switch commands is where the API will come in handy. In the inventory you can assign an ID to a particular service. Many subscription or billed services require an interval payment will need some way of turning on or off a particular service. The best way to do this is by using a switch command to produce a boolean output, which can then be integrated by the service into their interface via the API to do whatever they need it to do. Here is an example of a "Netflix" contract.

> for roll\[customers\]:

> take 7.99 every(t + 365/12),

> start(365/12),

> if(!take\[1\]):

> switch

**msg** statements will allow a text notification to be sent both within the directory but also via SMS and email.

> for roll\[subscribers\]:

> msg.email("Thank you for subscribing!"),

> take 10 every(t + 365/12),

> if(!take\[1\]):

> msg.sms("Please add more to your wallet. We will try again next week."),

> take 10 on(t + 7),

> if(!take\[2\]):

> switch,

> exit.

> else:

> continue.

Since users of a status level above a certain point will have verified their identity via email and phone, the msg statement will pick this up for the contractor automatically and send it to the supplied contact point. However this will also appear as a notification in the directory. In this contract, when the user confirms the contract an email is sent thanking them for the subscription. The charge is 10 credits per month, and if the users wallet is empty, it sends them a message saying there will be another attempt next week. If this fails the switch command will be triggered via the API, and the boolean will be turned 0 (it is up to the creator of this contract to define what happens on their end of the service). The **continue** keyword is triggered if **take\[2\]** is successful, and reverts back to the monthly charge as per **take\[1\].**

The **exit** statement ends the contract and produces a receipt which is stored on the blockchain.

#### Special Keywords {#3daf .graf .graf--h4 .graf-after--p name="3daf"}

The **clause** statement is similar to a "function" in that it is a coherent unit of executable statements which can operate at the same time. This can closely mirror the functionality of contracts in the real world, which can have many clauses involved. It also means that Pax will be useful as a platform for extended bodies of cryptolaw, which clients can opt into by joining a roll. The syntax for clause blocks is **clause\[x\]: \_, \_, \_.** where x is the ordered number of clauses from 1 to x.

The **lock** statement allows both sides to put a deposit into the contract to secure it. This is one of the ways contractors in the future can ensure adherence to the contract in a global environment; sunk costs and skin in the game. An easy current example is large and complex transactions that require the contract to be secured, and also rent contracts where an agreed deposit is paid upfront. The syntax for the lock statement is **lock x** where x is the agreed lock amount in credits. The "hygiene" of executable contracts is notably different from didactic contracts; while Pax contracts allow for didactic features in the form of do statements, the main emphasis is on securing the contract in advance either by insuring it or naming an dispute resolution agency to resolve any disputes that emerge.

The **witness** statement allows you to add an ally in the directory who can oversee the contract. This can be an informal peer, to act as a guarantor in case the contract is broken (in which case the witness statement will be followed by a clause defining the contract logic to be followed in the case that happens. In more robust contracts, it will be possible to name an agency or professional advocate who will act as witness/guarantor. If the contract breaks, the dispute can then be resolved by that agency. When a contract is submitted, it produces a digest or summary of the contents which all parties of the contract digitally sign, including witnesses. Both individuals and agencies who are witnesses to a contract will see a digest and confirm their consent.

**status** is a consequential keyword which can add or take away status points, similar to a credit rating. Initially clients of the directory can raise their status by authenticating their account with social media and peer validation, to a maximum level of 0.5 status points (0.1 for each). After that status is earned through completed contracts and/or education.

The **ballot** command creates a referendum among all the members of a roll whenever it is invoked. Ballots are joined with **do** statements to denote the proposal or series of proposals to be voted on, which then creates a boolean "yes/no" option in the inventory of all the voters in the ballot. The best place to use this is in a **between** multilateral contract which involves a "many to many" agreement, but it can also be used to in other ways to resolve a disagreement using allies as a kind of jury. Rolls can be as long as users need them to be, so potentially ballots on the Pax platform could be used in the place of traditional voting systems, as is already being tested as Ukraine are using Ethereum contracts in their election. Unlike the standard ballot contract in Solidity, which can be found at<http://ether.fund/contract/1bfd0/ballot-in-solidity>, the Codex ballot command reduces a lot of the complexity, while being able to mix it into a broader context of clauses and conditionals.

his is an example of how a ballot contract can allow a group to decide whether to raise the fee in a club or lower. One side wants to raise the fee to 600 and the other wants to lower it to 400 in order to balance the budget.

> between roll\[club\]:

> clause\[1\]:

> ballot(do\[1\]: "This motion will raise the subscription fee to 600 credits per year"),

> (do\[2\]: "This motion will lower the subscription to 400 credits per year"),

> if do\[1\] \> do \[2\]:

> take 600 every(t + 365),

> else:

> take 400 every(t + 365).

> clause\[2\]:

> etc. etc.

In this way, Pax facilitates a form of democracy that is similar to the ancient Greek city-states or modern day Swiss cantons. Democracy can occur between any group of people on any particular contention over a shared interest, where there is consent to be governed by the outcome of the decision.

#### **Conclusion** {#be36 .graf .graf--h4 .graf-after--p name="be36"}

This is a very simple set of specifications which will nevertheless deal with a wide variety of use cases. All the keywords mentioned here will be backed by a web of Solidity contracts which will both service Codex commands via the Web3.js library, while also creating permanent digests and receipts of the contracts. The advantage of Pax is that it creates a high-trust environment which allows more people to enter into agreements safely and with accountability, while remaining completely voluntary: the best of both worlds.
