# termfrequency_inverse document frequency - tf_idf is a statistical method for determining how imp a word is to a document within a larger collection
# of document it combimes term frequency which measures how often a word appears in a document with inverse document frequency which measures how rare 
# or common a word is across a entire corpus

# Components of tf_idf
# -term frequency
# -inverse document frequency - log of total no of documents in the corpus divided by no of documents containing that specific term
                # - high tf high idf - a word that appears frequently in a document but is rare across the whole corpus
                # - lowtf high idf - a word that appears in a document but is not very common overall
                # - hightf Low idf - a common word that appears frequntly in a document but also in many other documents 1 