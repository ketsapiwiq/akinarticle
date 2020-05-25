---
title: "This Machine Turns Trump Tweets into Planned Parenthood Donations"
url: https://medium.com/@maxbraun/this-machine-turns-trump-tweets-into-planned-parenthood-donations-4ece8301e722#.okpho4ldl
keywords: donations,parenthood,youll,lot,work,algorithm,wrong,turns,planned,trump,fund,underlying,machine,tweets,gets,simulated,data
---
But does it actually work? Let's look at the numbers.

Check out the [benchmark report](https://github.com/maxbbraun/trump-correction/blob/master/benchmark.md){.markup--anchor .markup--p-anchor}. It's essentially a test run that shows you how the algorithm performs on past tweets and market data. You'll see that it sometimes misses a company or gets a sentiment wrong, but it also gets it right a lot. The trading strategy sometimes leaves you up and sometimes down.

Overall, the algorithm seems to succeed more often than not: The simulated fund has an annualized return of about 59% since inception. There are limits to the simulation and the underlying data, so take it all with a grain of salt.

![](https://cdn-images-1.medium.com/freeze/max/60/1*NSskzBDB9sL7udvjJkraTg.png?q=20){.progressiveMedia-thumbnail .js-progressiveMedia-thumbnail}![](https://cdn-images-1.medium.com/max/1600/1*NSskzBDB9sL7udvjJkraTg.png){.progressiveMedia-noscript .js-progressiveMedia-inner}The results of running a [simulated fund](https://github.com/maxbbraun/trump2cash/blob/master/benchmark.md#fund-simulation){.markup--anchor .markup--figure-anchor} with a \$100,000 initial investment

Think you can make it perform better? [Fork the code on GitHub](https://github.com/maxbbraun/trump2cash){.markup--anchor .markup--p-anchor}! There are a bunch of obvious things to improve and there's a lot of room for creative ideas. I started collecting a list of them [here](https://github.com/maxbbraun/trump2cash/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement){.markup--anchor .markup--p-anchor}.
