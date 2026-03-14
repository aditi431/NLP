# word =  "running"
# for i , char in enumerate(word):
#     if(char == i and char+1 == n and char == g):
#         word = char.length() - (word[i]+word[n]+word[g])
# print(word)

# Slicing

# token = word

# stemming_token = token[0:-3]

# print(stemming_token)

# for loop 

suffixes = ['ing','ed','es','ly','er','ness']
def bruteStem(word):
    for i in suffixes:
        if word.endswith(i):
            word = word[:-len(i)]
    return word

words = ["running","ran","easily","happiness","fairly"]
stemmed_words = [bruteStem(word) for word in words]
print(stemmed_words)


