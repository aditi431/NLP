import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
text = "this is. the example of text to tokenize"
#Sentence tokenization

sentence = sent_tokenize(text)
print(sentence)

# word tokenization

word = word_tokenize(text)
print(word)

# stemming , limitization(more accurate) - for pure root word 

# stemming is the process of reducing a word to its base form or pure form by removing prefixes or suffixes it may or may not generate a valid word
# eg - studies = studi

# Limitization - is the process of reducing a word to its pure form (lemma) or dictionary form using vocabulary and morphological analysis it
# considers the context and the part of speech to produce valid word Eg - playing - play , better is converted to good content suggest us comparative adjective
# The produce result is always a valid point