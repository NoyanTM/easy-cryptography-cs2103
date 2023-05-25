from Cryptodome.Cipher import DES3
from Cryptodome.Random import get_random_bytes

def encrypt_3des(key, plaintext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_3des(key, ciphertext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Generate a random 3DES key (24 bytes)
key = get_random_bytes(24)

# Plain text to be encrypted
plaintext = b'This is a secret message.'

# Encrypt the plaintext
ciphertext = encrypt_3des(key, plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_text = decrypt_3des(key, ciphertext)
print("Decrypted text:", decrypted_text.decode())
