# This is technique to send secret messages (encryption and decryption)
# Or encryption technique is Caesecipher (plain text -> Cipher text)-encryption and cipher text -> plain text - decryption
# Encryption formula - E(x) = (x + n)mod 26 x- position of letter like A,B , n -shift key
# Decryption formula - D(x) = (x - n)mod 26 if -ve than add 26
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position+shift_key
        cipher_text +=alphabet[new_position]
    print(f"Here's is the text after encryption: {cipher_text}")

def decryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position-shift_key
        cipher_text +=alphabet[new_position]
    print(f"Here's is the text after decryption: {cipher_text}")



What_to_do = input("Type encrypt for encrytion and decrypt for decryption:")
message = input("Type message : ")
shiftKey = int(input("Enter shift key : "))
if What_to_do == "encrypt":
    encryption(plain_text=message,shift_key=shiftKey)
elif What_to_do == "decrypt":
    decryption(plain_text=message,shift_key=shiftKey)
else:
    print("Unexpected String")





    

