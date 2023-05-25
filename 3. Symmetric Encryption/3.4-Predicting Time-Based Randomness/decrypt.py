import time
import random
from Crypto.Cipher import AES

def decrypt(encrypted_data, min_seed, max_seed):
    key = None
    plaintext = None
    for seed in range(min_seed, max_seed + 1):
        random.seed(seed)
        candidate_key = bytes([random.randint(0, 255) for _ in range(16)])
        cipher = AES.new(candidate_key, AES.MODE_EAX, nonce=encrypted_data[1])
        try:
            plaintext = cipher.decrypt_and_verify(encrypted_data[2], encrypted_data[3]).decode('utf-8')
            key = candidate_key
            break
        except ValueError:
            pass
    return key, plaintext

if __name__ == '__main__':
    encrypted_data = (b'\x83\x9elE\x01\x80B\x95\xa7X7\x11\xac\x84\xb7{', b';A\xf3O\x98\xb6\xbe3\xdd)*\xdb\xc1h\xde\xa5', b'\x87k\xe8\xe9]\xe>
    min_seed = round(time.time()) - 3600  # 1 hour ago
    max_seed = round(time.time()) + 3600  # 1 hour from now
    key, plaintext = decrypt(encrypted_data, min_seed, max_seed)
    if key is None:
        print('Failed to decrypt data!')
    else:
        print('Decrypted Data:', plaintext)
        print('Key:', key)
