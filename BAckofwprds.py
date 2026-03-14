#    nl p process technique that converts text into a numerical vector representation by this regarding grammar and word order focussing 
# only on the frequency of each word it creartes a back and count how often each word appears which is used by features like spam detection


# How back of words model work

import nltk 

from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    "natural language processing is fun",
    "nlp is powerfull",
    "lets learn nlp",
    "dice","dice","dice"
]

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(corpus)
print("vocabulary:",vectorizer.get_feature_names_out())
print("\nBow Representation : \n",x.toarray())