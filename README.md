# Akinarticle

An adaptation of the 20 questions game to create an Akinator for [bafe.fr](https://bafe.fr) articles.
20 questions game adapted from [Andy Freeland and Dan Levy's student project](https://github.com/rouge8/20questions).

## Run
To run the program, enter 'python run.py' into the terminal.

You can specify an optional port number, but by default it'll run on port 8080, so open http://localhost:8080/ in a web browser to access it. 

Admin pages can be reached at http://localhost:8080/admin

While playing, you can even use 'y', 'n', and 'u', to answer questions instead of clicking!

## Data collection process
> Needs automation

* Save from WebScraper Firefox extension by importing `bafe.webscraper` file
* Transform into `bafe.xlsx` in Excel or LibreOffice
* Export individual sheets *with LibreOffice* to UTF-8 CSV
* Transform to SQL with [sqlizer.io](https://sqlizer.io)
* Import into current SQLite databes with *DBeaver* or *DB Browser for SQLite*

## Resources
* OnevsRest: https://towardsdatascience.com/multi-label-text-classification-with-scikit-learn-30714b7819c5