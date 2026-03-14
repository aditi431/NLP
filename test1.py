# def brute(word):
#     lemma_dict ={
#     "studying" : "study",
#     "happening" : "happy",
#     "studies" : "study",
#     "easily" : "easy",
#     "slept" : "sleep"
#     }
#     if word in lemma_dict:
#         return lemma_dict[word]
#     if word.endswith("ing"):
#         return word[:-3]
    
#     elif word.endswith("ed"):
#         return word[:-2]
    
#     elif word.endswith("s"):
#         return word[:-1]
    
#     words = ["running","runs","emptiness","studying"]
#     for w in words:
#         print(f"{w:10s} -> {brute(w)}")

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag,word_tokenize
def wordnet(tag):
    if tag.startswith('3'):return wordnet.ADJ