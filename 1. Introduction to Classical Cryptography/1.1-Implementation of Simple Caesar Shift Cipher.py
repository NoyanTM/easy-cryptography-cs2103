def caesar_cipher(msg, shift):
        res = '' # resulted encrypted cipher text
        for char in msg:
                if char.isalpha(): # checking if it is alphabet letter
                        if char.isupper(): # checking if it is uppercase letter
                                res += chr((ord(char) + int(shift) - 65) % 26 + 65)
                        else: # char is lowercase and would change according ascii position of letter symbol
                                res += chr((ord(char) + int(shift) - 97) % 26 + 97)
                else:
                        res += char # char would remain same
        return res

msg = input('Enter your message: ')
shift = input('Enter your shift: ')
print('Plaintext message: ', msg)
print('Shift pattern: ', shift)
print('Encrypted message: ', caesar_cipher(msg, shift))
