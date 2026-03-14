import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
text = "i am learning nlp in the classroom"
tokens = word_tokenize(text.lower())
stop_word = { 'i '
, 'am'    
}



# stop_words = set(stopwords.words("english"))
filter_tokens = [w for w in tokens if w not in stop_words ]
print("original tokens : ",tokens)
print("after removal of stop words : ",filter_tokens)