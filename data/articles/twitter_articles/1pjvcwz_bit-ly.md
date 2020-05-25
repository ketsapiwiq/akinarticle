---
title: "Three and a half degrees of separation"
url: http://bit.ly/1PjVcwz
keywords: person,degrees,separation,half,connected,number,hash,facebook,average,estimate,friends
---
"I read somewhere that everybody on this planet is separated by only six other people. Six degrees of separation. Between us and everybody else on this planet. The president of the United States. A gondolier in Venice. Fill in the names. . . . How every person is a new door, opening up into other worlds. Six degrees of separation between me and everyone else on this planet. But to find the right six people . . ." -- John Guare, [Six Degrees of Separation](https://en.wikipedia.org/wiki/Six_Degrees_of_Separation_(play)) (1990)

How connected is the world? Playwrights \[1\], poets \[2\], and scientists \[3\] have proposed that everyone on the planet is connected to everyone else by six other people. In honor of Friends Day, we've crunched the Facebook friend graph and determined that the number is 3.57. **Each person in the world (at least among the 1.59 billion people active on Facebook) is connected to every other person by an average of three and a half other people.** The average distance we observe is 4.57, corresponding to 3.57 intermediaries or "degrees of separation." Within the US, people are connected to each other by an average of 3.46 degrees.

Our collective "degrees of separation" have shrunk over the past five years. In 2011, researchers at Cornell, the Università degli Studi di Milano, and Facebook computed the average across the 721 million people using the site then, and found that it was 3.74 \[4,5\]. Now, with twice as many people using the site, we've grown more interconnected, thus shortening the distance between any two people in the world.

Calculating this number across billions of people and hundreds of billions of friendship connections is challenging; we use statistical techniques described below to precisely estimate distance based on de-identified, aggregate data.

Some Facebook employees
-----------------------

![post00006\_image0002](https://research.fb.com/wp-content/uploads/2016/11/post00006_image0002.jpg){.alignnone .wp-image-347 width="118" height="118"}

[Mark Zuckerberg](https://www.facebook.com/zuck)\
**3.17** degrees of separation

![post00006\_image0003](https://research.fb.com/wp-content/uploads/2016/11/post00006_image0003.jpg){.alignnone .size-full .wp-image-348 width="118" height="118"}

[Sheryl Sandberg](https://www.facebook.com/sheryl)\
**2.92** degrees of separation

The majority of the people on Facebook have averages between 2.9 and 4.2 degrees of separation. Figure 1 (below) shows the distribution of averages for each person.

![post00006\_image0004](https://research.fb.com/wp-content/uploads/2016/11/post00006_image0004.png){.alignnone .size-full .wp-image-349 width="1024" height="524"}

Figure 1. Estimated average degrees of separation between all people on Facebook. The average person is connected to every other person by an average of 3.57 steps. The majority of people have an average between 3 and 4 steps.

Calculating degrees-of-separation at scale
------------------------------------------

Calculating degrees of separation in a network with hundreds of billions of edges is a monumental task, because the number of people reached grows very quickly with the degree of separation.

Imagine a person with 100 friends. If each of his friends also has 100 friends, then the number of friends-of-friends will be 10,000. If each of those friends-of-friends also has 100 friends then the number of friends-of-friends-of-friends will be 1,000,000. Some of those friends may overlap, so we need to filter down to the unique connections. We're only two hops away and the number is already big. In reality this number grows even faster since most people on Facebook have more than 100 friends. We also need to do this computation 1.6 billion times; that is, for every person on Facebook.

Rather than calculate it exactly, we relied on statistical algorithms developed by Kang and others \[6-8\] to estimate distances with great accuracy, basically finding the approximate number of people within 1, 2, 3 (and so on) hops away from a source.

More accurately, for each number of hops we estimate the number of distinct people you can reach from every source. This estimation can be done efficiently using the Flajolet-Martin algorithm \[9\]. How does it work? Imagine you have a set of people and you want to count how many are unique. First you assign each person a random integer; let's call it hash. Approximately 1/2 of the people will have an even hash: the binary representation of the hash will end with 0. Approximately 1/4 of the people will have a hash divisible by 4; that is, the binary representation ends with 00. In general, 1/2n people will have the binary representation of their hash end with n zeros. Now, we can reverse this and try to count how many different people we have by reading their hash values one by one. To do that, we track the biggest number of zeroes we've seen. Intuitively, if there were n zeroes, we can expect set to have c\*2n unique numbers, where c is some constant. For better accuracy we can do this computation multiple times with different hash values.

This algorithm maps well to our problem: you just find the biggest number of zeroes among all friends' hashes. By using a bitwise OR operation on the hash, this process can be repeated recursively to estimate the number of unique friends-of-friends, and then friends-of-friends-of-friends. We used Apache Giraph \[10\] to run this computation on the entire Facebook friendship graph. In our implementation, at each step each person sends a bitwise ORed hash value to all his friends. We do this recursively and use Flajolet-Martin's math to estimate the number of unique friends for each degree of separation.

In summary, we find that the world is more closely connected than you might think.

By Sergey Edunov (3.46), Carlos Greg Diuk (3.16), Ismail Onur Filiz (3.33), Smriti Bhagat (3.32), and Moira Burke (3.35)

Cover image by Diana MacLean (3.26)

References
----------

\[1\] [Six Degrees of Separation (play) -- Wikipedia](https://en.wikipedia.org/wiki/Six_Degrees_of_Separation_(play))\
\[2\] [Frigyes Karinthy -- Wikipedia](https://en.wikipedia.org/wiki/Frigyes_Karinthy)\
\[3\] [Small-world experiment -- Wikipedia](https://en.wikipedia.org/wiki/Small-world_experiment)\
\[4\] Backstrom, L., Boldi, P., Rosa, M., Ugander, J., & Vigna, S. (2012). [Four degrees of separation](http://arxiv.org/abs/1111.4570). Proceedings of the 4th Annual ACM Web Science Conference, 33-42.\
\[5\] Ugander, J., Karrer, B., Backstrom, L., & Marlow, C. (2011). [The anatomy of the Facebook social graph](http://arxiv.org/abs/1111.4503).\
\[6\] Kang, U., Papadimitriou, S., Sun, J., Tong H. (2011). [Centralities in Large Networks: Algorithms and Observations](http://www.cs.cmu.edu/~ukang/papers/CentralitySDM2011.pdf). Proceedings of the SIAM International Conference on Data Mining.\
\[7\] Palmer, C., Gibbons, P., & Faloutsos, C. (2002). [ANF: A fast and scalable tool for data mining in massive graphs](http://tinyurl.com/jtcrzeu). Proceedings of the eighth ACM SIGKDD international conference on Knowledge discovery and data mining. 81-90.\
\[8\] Cohen, E. (1997) [Size-estimation framework with applications to transitive closure and reachability](http://www.sciencedirect.com/science/article/pii/S0022000097915348). Journal of Computer and System Sciences 55(3): 441-453.\
\[9\] [Flajolet-Martin algorithm](https://en.wikipedia.org/wiki/Flajolet%E2%80%93Martin_algorithm)\
\[10\] <http://giraph.apache.org/>
