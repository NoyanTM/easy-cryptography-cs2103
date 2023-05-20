import string

def caesar_cipher(message, shift):
   # Library of ascii symbols (alphabet)
   alphabet = string.ascii_uppercase + string.ascii_lowercase

   # Mapping of each letter to their new shifted positions
   mapping = {}
   for i, letter in enumerate(alphabet):
       shifted_letter = alphabet[(i+shift) % len(alphabet)]
       mapping[letter] = shifted_letter

   # Encoding every letter with new mapping
   encoded_message = ""
   for letter in message:
       if letter in mapping:
           encoded_message += mapping[letter]
       else:
           encoded_message += letter
   return encoded_message

while True:
   option = input("What to do?\n1. Encrypt\n2. Decrypt\n3. Exit \nChoose options from 1 to 3: ")

   if option not in ["1", "2", "3"]:
       print("Invalid input")
       continue

   elif option == "3":
       break

   message = input("Enter a message: ")

   shift = int(input("Enter a shift value: "))

   if option == "1":
       encrypted_message = caesar_cipher(message, shift)
       print("Encrypted message:", encrypted_message)

   else:
       decrypted_message = caesar_cipher(message, -shift)
       print("Decrypted message:", decrypted_message)
