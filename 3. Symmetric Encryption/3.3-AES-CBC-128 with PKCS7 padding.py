from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.primitives import hashes
import os


# Padding data
def pad_data(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data


# Unpadding data
def unpad_data(data):
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(data) + unpadder.finalize()
    return unpadded_data


# AES-CBC Encryption
def aes_cbc_encrypt(key, iv, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_plaintext = pad_data(plaintext)
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return ciphertext


# AES-CBC Decryption
def aes_cbc_decrypt(key, iv, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadded_data = unpad_data(decrypted_data)
    return unpadded_data


key = os.urandom(16)  # Random key (16 bytes / 128 bits)
iv = os.urandom(16)  # Random IV (16 bytes / 128 bits)
plaintext = b'This is the plaintext message'

# Example of output
encrypted_data = aes_cbc_encrypt(key, iv, plaintext)
decrypted_data = aes_cbc_decrypt(key, iv, encrypted_data)
print("Encrypted data:", encrypted_data.hex())
print("Decrypted data:", decrypted_data.decode())
