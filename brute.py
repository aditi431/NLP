import nltk
from nltk.stem import PorterStemmer , SnowballStemmer
words = ["running","runs","studies","studying"]
porter = PorterStemmer()
snowball = SnowballStemmer("english")
print("words  |porter stemmer | snowball stemmer ")
for w in words:
    print(f"{w:10s} | {porter.stem(w):13s} | {snowball.stem(w):15s}")