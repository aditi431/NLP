# Higher order functions:
'''
These are the functions that take other functions or return other functions 

'''

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func):
    return func("hello")

print(speak(shout))
print(speak(whisper))