from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import itertools

def brute_force_rsa(key, ciphertext):
    plaintexts = [''.join(i) for i in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=4)]
    for plaintext in plaintexts:
        if cipher.decrypt(ciphertext).decode('utf-8') == plaintext:
            return plaintext
    return None

key = RSA.generate(1024)
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(b'aitu')
plaintext = brute_force_rsa(key, ciphertext)
print(plaintext)
