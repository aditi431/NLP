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
        if ('hello') in tokens:
            print("Hi! How can I assist you?")
        elif ('how') in tokens:
            print("I am good! How about you?")
        elif ("thank") in tokens:
            print("Glad helping you!")
            break
        else:
            print("please re-enter")

chatbot_response()