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

# Sklearn
from sklearn.decomposition import LatentDirichletAllocation, TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from pprint import pprint

# %%
# Plotting tools
import pyLDAvis
import pyLDAvis.sklearn
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.metrics import calinski_harabaz_score

from collections import Counter

# %% [markdown]
# <h1>Load in Dataset

# %%
df = pd.read_json('data/articles/readable_bafe.jsonl', lines=True)

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
df.plain_content = df.plain_content.replace(pat, '')

# %%
df.head()

# %% [markdown]
# <h3>Tokenize

# %%
df.plain_content = df.plain_content.str.lower()


# %%
df['tokenized_content'] = df.plain_content.apply(lambda x: word_tokenize(x, language = 'french') if x else x)

# %%
df.head()

# %% [markdown]
# <h3>Remove Stop Words

# %%
stops = list(set(stopwords.words('french'))) + list(punctuation) + []

# %%
#function to remove stop words
def remove_stops(text):
    text_no_stops = []
    for i in text:
        if i not in stops:
            if len(i) == 1:
                pass
            else:
                text_no_stops.append(i)
        else:
            pass
    return text_no_stops


# %%
df['no_stops_content'] = df['tokenized_content'].apply(lambda x: remove_stops(x) if x else x)


# %%
#verify that it worked
df.head()

# %% [markdown]
# ### Lemmatization

# %%
#lemmatizer = nltk.stem.WordNetLemmatizer()
import spacy
spacy_french = spacy.load('fr_core_news_md')

# %%
#function to lemmatize text
def lemmatize_list(list):
    lemmatized = []
    for word in list:
        doc = spacy_french(word)
        for item in doc:
            lemmatized.append(item.lemma_)
    return lemmatized


# %%
df['lemmatized_content'] = df['no_stops_content'].apply(lemmatize_list)


# %%
# Should fix the string to list to string again, especially since spacy doesn't need it
df['lemmatized_content'] = df['lemmatized_content'].apply(lambda x: ' '.join(x))


# %%
df.head()


# %%
#Checkpoint -- save to csv
df.to_csv('df_with_lemmings.csv')

# %% [markdown]
# <h3>KMEANS CLUSTERING

# %%
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from langdetect import detect
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import words
from nltk.tokenize import RegexpTokenizer
import ast

# %% [markdown]
# <h3> Detect languages of articles

# %%
df['language'] = df['lemmatize_first_100'].apply(detect)


# %%
df.groupby('language').count()


# %%
#drop rows that are not english
df = df.loc[df['language'] == 'en']


# %%
#df.to_csv('df_english_articles.csv')

# %% [markdown]
# <h3>Modeling

# %%
df = pd.read_csv('../Data/df_english_articles.csv')


# %%
stemmer = PorterStemmer()


# %%
#create function to stem each word in a list and concat the list
def stem_list(lst):
    stemmed_list = []
    for i in lst:
        stemmed_list.append(stemmer.stem(i))
    stem_string = ' '.join(stemmed_list)
    return stem_string


# %%
#convert list contained in string to a regular list so it can be stemmed
df['stemmed'] = df["first_100_no_stops"].apply(lambda x: ast.literal_eval(x))


# %%
#stem words in list
df['stemmed'] = df["stemmed"].apply(lambda x: stem_list(x))


# %%
#verify that it worked
#df.head()


# %%
#drop specific duplicate rows
df = df[~df['stemmed'].str.contains("archiveteam.org contain", case=False)]


# %%
df.shape


# %%
#CHECKPOINT --- SAVE TO CSV
#df.to_csv('df_with_stems_final.csv')

