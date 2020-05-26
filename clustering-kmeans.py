# %%
#CHECKPOINT --- RUN TO OPEN CSV IF STARTING WORK HERE
#df = pd.read_csv('df_with_stems_final.csv')
#df.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace = True)


# %%
#df.head()


# %%
#create list of stemmed document strings
documents = df['stemmed'].to_list()


# %%
#preview list
#documents[:3]


# %%
#function to vectorize strings and perform tf-idf transformation
def vectorize_texts(list_of_strings):
    print('Performing vectorization and TF/IDF transformation on texts...')
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(list_of_strings)
    transformer = TfidfTransformer(smooth_idf=False)
    tfidf = transformer.fit_transform(X)
    return tfidf


# %%
def cluster_texts(num_clusters, tfidf):
    #perform kmeans clustering for range of clusters
    print('Beginning KMeans Clustering, number of clusters = ', num_clusters, '\n') 
    km = KMeans(n_clusters=num_clusters, max_iter = 100, verbose = 2, n_init = 1).fit(tfidf)
    
    
    return km

# %% [markdown]
# <h3>Run Clustering for range of K's

# %%
#vectorized the list of stemmed documents
documents_vectorized = vectorize_texts(documents)


# %%
#kmeans3 = cluster_texts(3, documents_vectorized)


# %%
#kmeans4= cluster_texts(4, documents_vectorized)


# %%
#kmeans5= cluster_texts(5, documents_vectorized)


# %%
#kmeans6= cluster_texts(6, documents_vectorized)


# %%
#kmeans7= cluster_texts(7, documents_vectorized)


# %%
#kmeans8= cluster_texts(8, documents_vectorized)


# %%
#kmeans9= cluster_texts(9, documents_vectorized)


# %%
#kmeans10= cluster_texts(10, documents_vectorized)


# %%
#kmeans11= cluster_texts(11, documents_vectorized)


# %%
#kmeans12= cluster_texts(12, documents_vectorized)


# %%
import pickle


# %%
#save kmeans12 model for further use
pickle.dump(kmeans12, open("../Models/kmeans12.pkl", "wb"))


# %%
#load back in kmeans12 model
#kmeans = pickle.load(open("kmeans12.pkl", "rb"))


# %%
kmeans_df = pd.DataFrame()


# %%
kmeans_df.columns = ['kmeans3', 'kmeans4', 'kmeans5', 'kmeans6', 'kmeans7', 'kmeans8', 'kmeans9', 'kmeans10', 'kmeans11', 'kmeans12']


# %%
kmeans_df['kmeans12'] = kmeans12.labels_


# %%
kmeans_df['stemmed'] = df['stemmed']


# %%
print(df.shape)
print(kmeans_df.shape)


# %%
#kmeans_df.head()


# %%
#CHECKPOINT --- SAVE TO CSV TO AVOID RUNNING KMEANS FUNCTIONS AGAIN
kmeans_df.to_csv('../Models/kmeans_df.csv')


# %%
kmeans_df = pd.read_csv('../Modelskmeans_df.csv')

# %% [markdown]
# <h3>Check Clusters for K's

# %%
kmeans_df['kmeans3'].value_counts()


# %%
kmeans_df['kmeans12'].value_counts()


# %%
ax = sns.countplot(x= 'kmeans12', data=kmeans_df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)


# %%
#function to find the most common words within each cluster
def get_most_common_words(df, df_column, num_words):
    common_words = []
    for i in range(0,12):
        common = Counter(" ".join(df.loc[df_column == i]['stemmed']).split()).most_common(num_words)
        for j in common:
            dict_ = {}
            dict_['cluster'] = i
            dict_['word'] = j[0]
            common_words.append(dict_)
            
    return common_words    
            


# %%
get_most_common_words(kmeans_df, kmeans_df['kmeans12'], 25)


# %%
Counter(" ".join(kmeans_df.loc[kmeans_df['kmeans12'] == 9]['stemmed']).split()).most_common(10)


# %%
#check clusters manually
#kmeans_df.loc[kmeans_df['kmeans12'] == 9]['stemmed'][:10].values


# %%



# %%
X_test_2 = ["""He has been training populists in Italy and fomenting revolution in Belgium. He has been down in Texas,
building a wall. But these have all been halting projects, placeholders. The real question is whether Steve Bannon 
will be back by Donald Trump’s side in 2020, after a two-year exile from Trumpworld. That could happen, at least 
according to Trump himself. “I’ll tell you one thing,” Trump said when I asked him about Bannon in February, 
during an Oval Office interview. “I watched Bannon a few times, four or five times over the last six months. 
Nobody says anything better about me right now than Bannon. I don’t know.” Bannon, of course, was the mastermind who 
took over a faltering Trump campaign in August 2016, guiding it to improbable victory. He then served as Trump’s 
chief political strategist in the White House, only to be forced out by Trump’s second chief of staff, John Kelly, 
in a move that a plainly exhausted Bannon seemed to almost welcome after months of battling the president’s 
son-in-law, Jared Kushner, the president’s daughter Ivanka Trump and, well, pretty much everyone else."""]


# %%
def text_prep(sample_text):
    tokens = word_tokenize(str(sample_text), language = 'en')
    no_stops = remove_stops(tokens)
    stemmed = stem_list(no_stops)
    stemmed = stemmed.replace('\\n', '')
    return [stemmed]


# %%
text_prep(X_test_2)


# %%



# %%



# %%



# %%


# %% [markdown]
# <h3>Merge Kmeans12 into original df
#     

# %%
df_clusters = pd.concat([df, kmeans_df['kmeans12']], axis = 1, sort = False)


# %%
#df_clusters.head(100)


# %%
#overwrite previous csv with clusters df
df_clusters.to_csv('../Data/df_english_articles.csv')


# %%
df_clusters.shape

# %% [markdown]
# <h3>Re-Cluster Cluster #3

# %%
kmeans12_cluster3 = pd.DataFrame(df_clusters['kmeans12'].loc[df_clusters['kmeans12'] == 3])


# %%
kmeans12_cluster3['stemmed'] = kmeans_df['stemmed']


# %%
kmeans12_cluster3


# %%
documents_cluster3 = kmeans12_cluster3['stemmed'].to_list()


# %%
cluster_3_vectorized = vectorize_texts(documents_cluster3)


# %%
kmeans10_cluster3= cluster_texts(10, cluster_3_vectorized)


# %%
kmeans_10_cluster3 = pd.DataFrame(kmeans10_cluster3.labels_)


# %%
kmeans_10_cluster3['stemmed'] = kmeans_df['stemmed']


# %%
kmeans_10_cluster3[0].value_counts()


# %%
get_most_common_words(kmeans_10_cluster3, kmeans_10_cluster3[0], 25)

# %% [markdown]
# After reviewing the top words in each of the clusters, they all seem to be political. This leads me to believe that cluster 3 in fact was properly clustered considering the articles were pulled from 2012-2017, right in the midst of the 2016 election period. Going forward, I will add more non-political articles to the dataset in order to adjust the class imbalance. 

# %%



