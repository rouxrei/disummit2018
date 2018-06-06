# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 08:43:32 2018

@author: reinert [dot] roux [at] xplodata [dot] be
"""

import nltk
from nltk.stem import PorterStemmer
from collections import Counter
import unicodedata


def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")


#•	Quick intro to working with text data (5 min)
#o	cleaning
#o	language 
#o	encodings
#
#•	Natural Language Processing (10-15 min)
#o	Stemming
#o	Part-of-speech tagging
#o	Tokenization
#o	Lemmatization
#o	Entity Recognition
#
#•	Quick overview of "Higher level" algorithms (to give an idea of the possibilities) (5 min)
#o	Sentiment Analysis
#o	Topic Detection
#o	Document classification

#POS tag list:
#
#CC	coordinating conjunction
#CD	cardinal digit
#DT	determiner
#EX	existential there (like: "there is" ... think of it like "there exists")
#FW	foreign word
#IN	preposition/subordinating conjunction
#JJ	adjective	'big'
#JJR	adjective, comparative	'bigger'
#JJS	adjective, superlative	'biggest'
#LS	list marker	1)
#MD	modal	could, will
#NN	noun, singular 'desk'
#NNS	noun plural	'desks'
#NNP	proper noun, singular	'Harrison'
#NNPS	proper noun, plural	'Americans'
#PDT	predeterminer	'all the kids'
#POS	possessive ending	parent's
#PRP	personal pronoun	I, he, she
#PRP$	possessive pronoun	my, his, hers
#RB	adverb	very, silently,
#RBR	adverb, comparative	better
#RBS	adverb, superlative	best
#RP	particle	give up
#TO	to	go 'to' the store.
#UH	interjection	errrrrrrrm
#VB	verb, base form	take
#VBD	verb, past tense	took
#VBG	verb, gerund/present participle	taking
#VBN	verb, past participle	taken
#VBP	verb, sing. present, non-3d	take
#VBZ	verb, 3rd person sing. present	takes
#WDT	wh-determiner	which
#WP	wh-pronoun	who, what
#WP$	possessive wh-pronoun	whose
#WRB	wh-abverb	where, when

# shorthand POS tag lists:
adj = ['JJ', 'JJR', 'JJS']
noun = ['NN', 'NNS', 'NNP', 'NNPS']
adverb = ['RB', 'RBR', 'RBS']
verb = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

# read input as bytes
raw_input = b''
path = r'.\data\output_txt\raw_Tanzania_SummarySheet_English.txt'
with open(path, 'rb') as input_file:
    raw_input =  input_file.read()

# 'guess' encoding    
import chardet
encodings = chardet.detect(raw_input)

# decode https://docs.python.org/3/library/codecs.html#standard-encodings
input_text_mac = raw_input.decode('mac_roman')
input_text_iso = raw_input.decode('8859')

# continue with the iso decoded string
#text = remove_control_characters(input_text_iso)
text = input_text_iso

# guess language
from langdetect import detect
language = detect(text)

# tokenize
tokens = nltk.word_tokenize(text)

# POS
tagged_text = nltk.pos_tag(tokens)
c = Counter([tag for (token, tag) in tagged_text])

# interesting tokens
i_tokens = [token for (token, tag) in tagged_text if tag in adj + noun + adverb + verb]

# stem tokens
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in i_tokens]

# Wordcloud https://python-graph-gallery.com/wordcloud/
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)

wordcloud = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=200,
                          max_font_size=40, 
                          random_state=42
                         ).generate(' '.join(i_tokens))

plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()


stemmed_wordcloud = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=200,
                          max_font_size=40, 
                          random_state=42
                         ).generate(' '.join(stemmed_tokens))
plt.figure(2)
plt.imshow(stemmed_wordcloud)

plt.axis('off')
plt.show()