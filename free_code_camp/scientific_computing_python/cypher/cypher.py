text_1 = 'Hello World'
text_2 = 'Hello Zaira'
text_3 = 'Albatross'
shift = 3

# If I'm correct i can use a parameter to enter the different texts into the caesar function

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            # If the char is a space we can skip it by adding 1 to char to reach the next char:
            encrypted_text += char
        else:
            index = alphabet.find(char)
            # Make sure the X, Y and Z are linked to the remainder/beginning of the alphabet:
            new_index = (index + offset) % len(alphabet)
            # Update encrypted text to char + 3:
            encrypted_text += alphabet[new_index]
    # Print the original text:
    # print('plain text:', text_2)        
    # Print only the encrypted text:        
    print('encrypted text:', encrypted_text)