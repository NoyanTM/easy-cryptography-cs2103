from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.primitives import hashes
import os


# Padding data
def pad_data(data):
    padder = padding.PKCS7(128).padder() # Defining padder instance
    padded_data = padder.update(data) + padder.finalize() # Updating padder with data and finalizing it
    return padded_data


# Unpadding data
def unpad_data(data):
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(data) + unpadder.finalize()
    return unpadded_data


# AES-ECB Encryption
def aes_ecb_encrypt(key, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend()) # Defining aesCipher object
    encryptor = cipher.encryptor() # Applying .encryptor() 
    padded_plaintext = pad_data(plaintext) # Calling padder function to plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize() # Finalizing aesCipher with padder
    return ciphertext


# AES-ECB Decryption
def aes_ecb_decrypt(key, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor() # Applying .decryptor() 
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadded_data = unpad_data(decrypted_data)
    return unpadded_data

key = os.urandom(16) # Defining randomed key (16 bytes / 128 bits)
plaintext = b'This is the plaintext message'

# Example of output
encrypted_data = aes_ecb_encrypt(key, plaintext)
decrypted_data = aes_ecb_decrypt(key, encrypted_data)
print("Encrypted data:", encrypted_data.hex())
print("Decrypted data:", decrypted_data.decode())
