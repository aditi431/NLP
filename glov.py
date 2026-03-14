import gensim.downloader as api # not give functionality as api
from numpy.linalg import norm
import numpy as np
glove = api.load("glove - wiki - gigaword -100 ") # no. of dimensions

# Word Similarity 
print("Similarity between king and queen",glove.similarity("king","queen"))
print("Similarity between dog and cat",glove.similarity("dog","cat"))
print("Similarity between dog and car",glove.similarity("dog","car"))
result = glove.most_similar(positive = ["king","woman"], negative = ["king","woman"])
print("\n anology : king - man+woman = ?")
# Sentence Embedding
def sentence_embedding(sentence):
    words = sentence.lower().split()
    vectors = [glove[w] for w in words if w in glove]
    if not vectors:
        return np.zeros(glove.vector_size)
    
# example sentence
sent1 = "man is walking on the street"
sent2 = "the baby is crying"

# cosine similarity between sentences
def cosine_similarity(vec1,vec2):
    return np.dot(vec1,vec2)
cosine_similarity(sentence_embedding(sent1),sentence_embedding(sent2))
print("Similartiy between : '{sent1}' \n '{sent2}' \n = {sim:.4f}")
