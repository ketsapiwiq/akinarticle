# TWENTY QUESTIONS FINAL PROJECT WRITE-UP

Andy Freeland and Dan Levy

June 6, 2010

## Description

Our program implements a version of 20 questions. It does so by having a table of objects and a table of questions and having another table with a correlation between objects and questions. Depending on a user's answers, the computer guesses the object which has the most correlation with the questions asked.

The hardest part of designing our algorithm was the part that chooses questions. Just like in a real 20 questions game, if you ask silly questions, you will not learn anything after you have asked 20 questions. Thus, we needed to make an algorithm to ask intelligent questions. The motivation behind asking a question is to effectively cut the number of candidates in half after each question. Thus, we wanted to choose a question such that half of the answers would be no for the objects and half of the answers would be yes for the other half of the objects. We did not want to ask questions where we did not have any correlation, so we originally weighed an unsure answer as 10 yeses.

However, that was not always giving us questions that we felt made sense, so we wrote a new entropy function where entropy is calculated similarly to in decision trees. The main difference is that we take the reciprocal of this value, as we _want_ questions where yes and nos are roughly evenly split. We could, rather than using reciprocals, take the maximum entropy, but when we initially wrote that function we weren't sure if it would be any good and so we had it return reciprocals so that it the code of choose_question wouldn't have to change for different entropy functions. This entropy function avoids asking questions with many unsure answers by weighting the pre-reciprocal values by (yeses+nos)/unsures.

Initially we ask up to four questions: 'Is the character real?,' up to two random questions, and 'Is the character a man?' in order to gather more information and because existence and gender are pretty important to know.

Our program is pretty good at guessing recently added objects. Some of the earlier ones are somewhat broken from a bug we had where we would learn wrong information. We didn't want to delete everything though, because we spent about 3-4 hours in Sayles having people play it, and we did not feel like we had time to reconstruct our database using the records (stored in the playlog table) we create of each game. If we had more time, we might have explored this possibility more.

Beyond the main game logic, we used the python library web.py to create a web based version of the game. We added various admin functions too, which can be accessed at /admin. In the future, we want to make the admin section have password protection, and we want to create a queue where we can approve suggested objects and questions instead of allowing them to be directly added to the database by users.

Error handling is minimal at the moment, because whenever something has crashed, that has been incredibly helpful in finding bugs (for obvious reasons). Everything that has caused crashes has been fixed, and things that are likely to raise exceptions have been put in Try/Except blocks, but it's entirely likely there are things we never managed to break that will still raise exceptions.

The web interface currently displays the list of characters being considered AND the value it has for them at any given stage, which we think is kind of cool.

## To Run
To run the program, enter 'python webinterface.py' into the terminal.

You can specify an optional port number, but by default it'll run on port 8080, so open http://localhost:8080/ in a web browser to access it. admin pages can be reached at http://localhost:8080/admin
While playing, you can even use 'y', 'n', and 'u', to answer questions instead of clicking!

Requires SQLite3, which is included in Python on OS X, Windows, and Linux.

Due to a bug in the version of PySQLite that ships with OS X Leopard, our code won't run on any of the labs. It does however, run on prism. We tested primarily on Linux with Python 2.6.2 and SQLite 3.6.20. It also works on Windows 7 with the Python 2.6.4 download from python.org. As we don't have Windows XP or other version of Python, we were unable to test it on them.

## The Future
Along with the improvements that we want to make (as described above), we want to find our program a home on the internet so people can play anytime!
