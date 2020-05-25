---
title: "More than a Million Pro-Repeal Net Neutrality Comments were Likely Faked"
url: https://hackernoon.com/more-than-a-million-pro-repeal-net-neutrality-comments-were-likely-faked-e9f0e3ed36a6
keywords: submission,likely,comments,word,million,neutrality,faked,prorepeal,used,vectors,clusters,submissions,net,text
---
#### Additional Notes: {#efae .graf .graf--h4 .graf--leading name="efae"}

-   [There have been some great analyses focused on the non-textual elements of the submissions, for example, their timing, the email addresses used, and other metadata. Shout out to the work of Jeffrey Fossett, who did [a first pass analysis of the partially submitted comments](http://jeffreyfossett.com/2017/05/13/fcc-filings.html){.markup--anchor .markup--li-anchor} in May that inspired this post and some of the methods used in the analysis, to [Chris Sinchok](https://medium.com/@csinchok/an-analysis-of-the-anti-title-ii-bots-463f184829bc){.markup--anchor .markup--li-anchor}, [GravWell](https://www.gravwell.io/blog/discovering-truth-through-lies-on-the-internet-fcc-comments-analyzed){.markup--anchor .markup--li-anchor}, and many other posts I studied in preparing this analysis.]{#0ab6}
-   [Let me know [here](https://www.jeffykao.com/contact/){.markup--anchor .markup--li-anchor} if you have any questions or would like access to the dataset I scraped from the FCC's ECFS submission system --- if enough folks request it, I may host the dataset on Google BigQuery so you can run SQL queries on the \~64 GB dataset on your own.]{#c03c}

#### Footnotes: {#3bb3 .graf .graf--h4 .graf-after--li name="3bb3"}

¹ I.e., not from a spambot or part of an identified campaign.

² Full disclosure: I was a summer law clerk for Commissioner Clyburn in 2010, and though I greatly admire her recent work [championing net neutrality](https://motherboard.vice.com/en_us/article/mg4wv3/how-mignon-clyburn-the-fccs-lone-democrat-is-fighting-to-save-net-neutrality){.markup--anchor .markup--p-anchor}, the opinions and POV in this post are my own.

³ Not clustered as part of a comment submission campaign, not a duplicate comment.

⁴ Data collected from beginning of submissions (April 2017) until Oct 27th, 2017. The long-running comment scraping script suffered from a couple of disconnections and I estimate that I lost \~50,000 comments because of it. Even though the Net Neutrality Public Comment Period ended on August 30, 2017, the FCC ECFS system continued to take comments afterwards, which were included in the analysis.

⁵ I used an md5 hash function, which had a [low enough collision rate](https://stackoverflow.com/questions/8852668/what-is-the-clash-rate-for-md5){.markup--anchor .markup--p-anchor} and allowed me to (relatively) quickly find and count up duplicates. I tossed out submissions with no express comment text but otherwise did not do any other text preprocessing on the text before encoding and clustering in order to preserve artifacts in the text that may give clues as to the method of submission.

⁶ A large proportion of these \~3 million "unique" comments were essentially duplicates --- only differing by a few characters or words or having a different signature. In order to conclusively and exhaustively categorize these comments, I chose to group comments by meaning. Comments were turned into document vectors comprised of the average of all word vectors in the comment. The word vectors were obtained from [spaCy](https://spacy.io/){.markup--anchor .markup--p-anchor}, which uses the word vectors from the paper by [Levy and Goldberg (2014)](http://www.aclweb.org/anthology/P14-2050){.markup--anchor .markup--p-anchor}. \[Correction from [Matthew Honnibal](https://twitter.com/honnibal){.markup--anchor .markup--p-anchor}: spaCy now uses the [GloVe](https://nlp.stanford.edu/projects/glove/){.markup--anchor .markup--p-anchor} vectors by Pennington et al.\]

⁷ I made two passes at clustering the document vectors. First with [DBSCAN](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html){.markup--anchor .markup--p-anchor} with a euclidean distance metric at a very low epsilon to identify obvious clusters \[Update on 11--25--2017: After reviewing old code & to give slightly more detail, I used [HAC](https://en.wikipedia.org/wiki/Hierarchical_clustering){.markup--anchor .markup--p-anchor} to pick out the mad-lib clusters\] and cull them out manually using a string signature. This left \~2 million unique comments. From that 2 million, I used [HDBSCAN](http://hdbscan.readthedocs.io/en/latest/api.html){.markup--anchor .markup--p-anchor} on a 100,000 comment sample with cosine distance to identify 'looser' clusters, and then used `approximate_predict()`{.markup--code .markup--p-code}to classify remaining comments as either within those identified clusters or as outliers. Removing duplicates, this resulted in less than 800,000 unique outlier "organic" comments. \[Correction: As HDBSCAN Author Leland McInnes notes below, cosine distances don't yet play well with HDBSCAN --- to be exact, I used the euclidean distance metric between l2-normalized doc vectors, which typically works well as a substitute.\]

⁸ Sized from the dozens to the millions.

⁹ Regular Expression in this [pastebin](https://pastebin.com/YvR0zjXy){.markup--anchor .markup--p-anchor}.

¹⁰ This is because the combinations of comment configurations grows exponentially with each set of synonyms introduced. Also, to be precise, there were some mad-lib comments that were duplicated once, but not more than that.

¹¹ Page 3 of [the Verizon Comments](https://ecfsapi.fcc.gov/file/1083064469202/2017%2008%2030%20Verizon%20Reply%20Comments%2C%202017%20Open%20Internet%20Notice.pdf){.markup--anchor .markup--p-anchor} (submitted August 30, 2017)

¹² FCC Chairman Pai's [Statement re the Draft Order](http://transition.fcc.gov/Daily_Releases/Daily_Business/2017/db1121/DOC-347868A1.pdf){.markup--anchor .markup--p-anchor} (published November 21, 2017)

¹³ While there are certainly other possible explanations for this set of results, I think [Occam's Razor](https://en.wikipedia.org/wiki/Occam%27s_razor){.markup--anchor .markup--p-anchor} should apply. More investigation into the timing and emails used for this particular campaign would provide more corroborating evidence.

¹⁴ Plotted on a log-scale so you can still see the color of the smaller bars.

¹⁵ As the author of the [Gravwell study](https://www.gravwell.io/blog/discovering-truth-through-lies-on-the-internet-fcc-comments-analyzed){.markup--anchor .markup--p-anchor} states: "\[The evidence\] forces us to conclude that either the very act of going to the FCC comment site and providing a comment is only attractive to those of a certain political leaning, or that the bulk submission information is full of lies."

¹⁶ Pro-repeal comments are on lines 176, 228, 930 in the [pastebin](https://pastebin.com/JGHy6tRu){.markup--anchor .markup--p-anchor}. There also appeared to be three net neutrality supporters that seemed confused about the terminology (lines 332, 366, 901) and one script kiddie (line 261). It's possible I have missed one or two, and I'm happy to correct any mistakes in this comment set if you find them.

¹⁷ My more statistically-inclined colleague informs me that the central limit theorem breaks down at the extreme limits (where the population proportion is near 0% or 100% of a population), which I have taken his word/expertise for, for now, and will learn about later. \[Edit: I have found a good addition to this on a [reddit comment](https://www.reddit.com/r/dataisbeautiful/comments/7f2sfy/natural_language_processing_techniques_used_to/dq9qzkh/){.markup--anchor .markup--p-anchor}. The interval is 99.12% to 99.90%, 19 times out of 20.\]

¹⁸ Line 102 in the [pastebin](https://pastebin.com/JGHy6tRu){.markup--anchor .markup--p-anchor}.

¹⁹ \[A final late addition: Lest I am unintentionally giving the wrong impression to folks who haven't been following the net neutrality debate as closely, I want to be clear that there were suspicious campaigns from all sides of the debate from the text-only analysis; however, none were as numerous and as intentionally disguised as the 1.3M 'unique' comments identified in the post.\]
