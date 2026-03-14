# import nltk
# from nltk.util import ngrams
# from nltk.tokenize import word_tokenize
# text = "this is the sample to demonstrate n-gram generation"
# # tokens = word_tokenize(text)
# n = 2
# ngram_result = list(ngrams(tokens,n))
# print(ngram_result)

import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.util import ngrams
from nltk.stem import WordNetLemmatizer

def rootword(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

def chatbot_response():
    while(True):
        text = input()
        tokens = rootword(text)
        if ('hello') or ("hi") in tokens:
            print("Hi! How can I assist you?")
        elif ('how' or " you ") in tokens:
            print("I am good! How about you?")
        elif("thank ") in tokens:
            print("Glad helping you!")
            break            
        else:
            return "please re-enter"

chatbot_response()



