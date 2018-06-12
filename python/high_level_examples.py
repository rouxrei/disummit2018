# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 09:39:28 2018

@author: rouxrei
"""
import os
from langdetect import detect
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

cv_txt_path = r'C:\Users\rouxrei\Documents\Projects\CVtoStarter\data\working\keep20190601'

filenames = [os.path.join(cv_txt_path, filename) for filename in os.listdir(cv_txt_path) if filename[-4:] == '.txt']

en_files = []
nl_files = []
other_files = []
for filename in filenames:
    with open(filename, mode='rt', encoding='latin-1') as file:
        txt = file.read()
        lang = detect(txt)
        if lang == 'en':
            en_files.append(txt)
        elif lang == 'nl':
            nl_files.append(txt)
        else:
            other_files.append(txt)

en_vectorizer = CountVectorizer(stop_words='english')
en_X = en_vectorizer.fit_transform(en_files)
nl_vectorizer = CountVectorizer()
nl_X = nl_vectorizer.fit_transform(nl_files)

#from sklearn.feature_extraction.text import TfidfTransformer
#transformer = TfidfTransformer(smooth_idf=False)
#
#transformer.fit_transform(file_contents)

en_lda = LatentDirichletAllocation(n_components=4, max_iter=5,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)
en_lda.fit(en_X)

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
    print()
    
print_top_words(en_lda, en_vectorizer.get_feature_names(), 20)
