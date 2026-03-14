import nltk
from nltk.stem import PorterStemmer, SnowballStemmer

from nltk.tokenize import sent_tokenize, word_tokenize
text = input("Enter text")
sentence = sent_tokenize(text)
print(sentence)
words = word_tokenize(text)
print(words)
# words = ["running", "runs", "studies", "studying"]
porter = PorterStemmer()
snowball = SnowballStemmer("english")
print("words       | porter stemmer | snowball stemmer ")
for w in words:
    print(f"{w:10s} | {porter.stem(w):13s} | {snowball.stem(w):15s}")