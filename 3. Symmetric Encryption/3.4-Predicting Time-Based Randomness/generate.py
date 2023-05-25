import time
import random
from Crypto.Cipher import AES

def encrypt(message):
    key = generate_key()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    return (key, nonce, ciphertext, tag)

def generate_key():
    seed_value = round(time.time())
    random.seed(seed_value)
    key = bytes([random.randint(0, 255) for _ in range(16)])
    return key

if __name__ == '__main__':
    message = 'This is a secret message!'
    encrypted_data = encrypt(message)
    print('Encrypted Data:', encrypted_data)
    print('Seed:', random.getstate()[1][0])
