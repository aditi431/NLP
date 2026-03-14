# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# words = ["running","files","better","rocks","studies","feet"]
# for word in words:

#     # POS tagging technique

#     lemma_word = lemmatizer.lemmatize(word,pos = 'v')
#     if lemma_word == word:
#         lemma_word = lemmatizer.lemmatize(word,pos ='n')
#     print(lemma_word)
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["files","file"]
for word in words:
    stemmed_words = stemmed.stem(word)
    print(stemmed_words)

