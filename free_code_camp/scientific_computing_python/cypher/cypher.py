text_1 = 'Hello World'
text_2 = 'Hello Zaira'
text_3 = 'Albatross'
custom_key = 'python'

# What if we could use a different key  for every char? then our message would be much more secure encrypted!

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        # check if a character is NOT an alphanumeric character:
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1
            # Define the offset and the encrypted letter:
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            # Make sure the X, Y and Z are linked to the remainder/beginning of the alphabet:
            new_index = (index + offset * direction) % len(alphabet)
            # Update encrypted text to char + 3:
            encrypted_text += alphabet[new_index]
    # Print the original text:
    # print('plain text:', text_2)        
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)
    
encryption = encrypt(text_1, custom_key)
print(encryption)
decryption = decrypt(encryption, custom_key)
print(decryption)