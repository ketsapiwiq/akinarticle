# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
# #nltk
#pip install any packages you don't have
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import WordNetLemmatizer

import numpy as np
import pandas as pd
import re, spacy, gensim


# %% [markdown]
# <h1>Load in Dataset

# %%
df = pd.read_json('data/articles/readable_bafe.jsonl', lines=True)


# %%
# If performance is an issue, only do first 100
preview = False
if (preview):
    df = df.head(100)

# %%
df = df.dropna(subset = ["plain_content"], axis='index', how='all')
#  drop superfluous columns
try:
    df = df.drop(['plain_text'], axis = 1)
except KeyError:
    pass
# %%
import re
pat = re.compile('<.*?>')
# Should operate on plain_content to delete all HTML tags.
df.plain_content = df.plain_content.replace(pat, ' ')
# delete apostrophe and separate
df.plain_content = df.plain_content.replace("’", ' ')
df.plain_content = df.plain_content.replace("'", ' ')

# %%
df.head()

# %% [markdown]
# <h3>Tokenize and lemmatize

# %%
spacy_french = spacy.load('fr_core_news_md')

# %%
#function to lemmatize text
def lemmatize_text(text):
    lemmatized = []
    nlp = spacy_french(text)
    for item in nlp:
        lemmatized.append(item.lemma_)
    return lemmatized

# %%
# Spacy nlp on entries

df['lemmatized_content_with_stop_words'] = df.plain_content.apply(lambda x: lemmatize_text(x))



# %%
#verify that it worked
df.head()
# Cimer la lemmatisation de "elle" c'est "lui"... Il faut regarder à plus loin avec les tags qu'offre spacy

#Checkpoint -- save to csv
if not preview:
    df.to_csv('df_with_lemmings_and_stopwords.csv')


# %% [markdown]
# <h3>Remove Stop Words

# %%
stops = list(set(stopwords.words('french'))) + list(punctuation) + ["l'","d'","n'","c'","j'","m'","s'","qu'", 'cela', 'faire', 'comme', 'avoir', 'être']

# %%
#function to remove stop words
def remove_stops(word_list):
    word_list_no_stops = []
    # print(word_list)
    if len(word_list) == 1:
        return word_list
    for word in word_list:
        if word not in stops and not (len(word) == 1):
            word_list_no_stops.append(word)
        else:
            pass
    return word_list_no_stops


# %%

df['lemmatized_content'] = df['lemmatized_content_with_stop_words'].apply(lambda x: remove_stops(x) if x else x)
# df['lemmatized_content'] = df['lemmatized_content_with_stop_words'].apply(lambda x: remove_stops(x) if x and not x == ' nan' else x)


# %%
#verify that it worked
df.head()



# %%
# recreate string
df['lemmatized_content'] = df['lemmatized_content'].apply(lambda x: ' '.join(x))


# %%

df['lemmatized_content'] = df['lemmatized_content'].str.lower()


# %%
df.head()


# %%
#Checkpoint -- save to csv
if not preview:
    df.to_csv('df_with_lemmings.csv')


# %%
from langdetect import detect
from nltk.corpus import words
from nltk.tokenize import RegexpTokenizer
import ast

# %% [markdown]
# <h3> Detect languages of articles

# %%
df['language'] = df['lemmatized_content'].apply(detect)


# %%
df.groupby('language').count()


# %%
#drop rows that are not french
df = df.loc[df['language'] == 'fr']


# %%
if not preview:
    df.to_csv('df_french_articles.csv')

# %% [markdown]
# <h3>Modeling


# %%
print(df.shape)
