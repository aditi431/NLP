# dictinary = {"run" :['ran','running','runs'], "happy" : ['happier','happiest','happily','happiness'],
# "sleep" : ['sleeping','slept','sleepy','sleepiness']
# "mood" : ['moody','moods']
# }

# def brute_force(word):
#     lemma_dict = {

#         'feet' : 'foot'
#         'mice' : 'mouse'
#         'geese': 'goose'
#         'went' : 'go'
#         'better': 'good'

# }
# if word in lemma_dict:
#     return lemma_dict[word]

# if word.endswith('ing') and len(word)


# nltk.stem module - porter stemmer

def brute_force(word):
    lemma_dict = {
        'feet' : 'foot',
        'mice' : 'mouse',
        'geese' : 'goose',
        'went' : 'go',
        'ran' : 'run',
        'better' : ' good'
    }
    
    if word in lemma_dict:
        return lemma_dict[word]
    
    if word.endswith('ing') and len(word) > 4:
        base = word[:-4]
        return base
    
    elif word.endswith('s') and len(word) > 2:
        return word[:-1]
    return word

text = "The kids are running and swimming better feet"
tokens = text.lower().split()
lematized_tokens = [brute_force(word) for word in tokens]
lematized_text = ''.join(lematized_tokens) 
print(lematized_tokens)

