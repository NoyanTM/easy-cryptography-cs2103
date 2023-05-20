message = 'This is program to explain reverse cipher.' # plaintext
translated = '' # stored ciphertext
i = len(message) - 1 
while i >= 0:
       translated = translated + message[i]
       i = i - 1
print('The cipher text is: ', translated)
