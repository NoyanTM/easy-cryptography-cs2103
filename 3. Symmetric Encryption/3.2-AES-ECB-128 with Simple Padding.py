from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Alice and Bob's Shared Key
test_key = bytes.fromhex('00112233445566778899AABBCCDDEEFF')

aesCipher = Cipher(algorithms.AES(test_key),
                   modes.ECB(),
                   backend=default_backend())
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

message = b'Hey Bob, let's meet up today at 23:00. How about grabbing a coffee and catching up? Oh, and I have exciting news to share with you as well! Looking forward to seeing you.'

message += b"E" * (-len(message) % 16)
ciphertext = aesEncryptor.update(message)

print("plaintext:",message)
print("ciphertext:",ciphertext.hex())
recovered = aesDecryptor.update(ciphertext)
print("recovered:",recovered)
if(message==recovered): print("[PASS]")
else: print("[FAIL]")
