# # Sentence tokenization

# text = "Hello! this is the implemantation of tokenization. using NLP."
# end_punctuation=[' , ','!','?','.']
# start = 0
# sentences = []

# for i , char in enumerate(text):
#     if char in end_punctuation:
#         sentence = text[start:i].strip()
#         if sentence:
#             sentences.append(sentence)
#             start = i+1

# print(sentences)



# Word tokeanization

text = "This is a word to$#$%keni%4#zation"
lst = ['$','#',"%",'()',"(",")","&","-","[","]","*"]
words = []
current_word = ''
for char in text:
    if char.isalnum():
        current_word+=char
    elif char in lst:
        words.append(char)
         
    else:
        if current_word:
            words.append(current_word)
            current_word = ''
if current_word:
    words.append(current_word)
print(words)




# text = "Hello! this is the implemantation of tokenization. using NLP."
# end_punctuation=(' , ','!','?','.')
# start = 0
# sentences = []

# for i , char in enumerate(text):
#     if char in end_punctuation:
#         sentence = text[start:i].strip()
#         if sentence:
#             sentences.append(sentence)
#             start = i+1

# print(sentences)



