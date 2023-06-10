from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import hashlib
import hmac

# Generate a random AES key
aes_key = get_random_bytes(16)

# Generate RSA key pair
rsa_key = RSA.generate(2048)

# Message to be encrypted
message = b"Hello, world!"

# AES encryption
cipher_aes = AES.new(aes_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(message)

# RSA encryption of AES key
cipher_rsa = PKCS1_OAEP.new(rsa_key.publickey())
encrypted_aes_key = cipher_rsa.encrypt(aes_key)

# Generate HMAC using SHA256
hmac_key = get_random_bytes(32)
hmac_hash = hmac.new(hmac_key, ciphertext, hashlib.sha256).digest()

# Print the encrypted AES key, ciphertext, and HMAC
print("Encrypted AES Key:", encrypted_aes_key)
print("Ciphertext:", ciphertext)
print("HMAC:", hmac_hash)

# RSA decryption of AES key
decipher_rsa = PKCS1_OAEP.new(rsa_key)
decrypted_aes_key = decipher_rsa.decrypt(encrypted_aes_key)

# Verify HMAC
hmac_verify = hmac.new(hmac_key, ciphertext, hashlib.sha256).digest()
if hmac_hash == hmac_verify:
    print("HMAC verified.")

# AES decryption
cipher_aes = AES.new(decrypted_aes_key, AES.MODE_EAX, cipher_aes.nonce)
decrypted_message = cipher_aes.decrypt_and_verify(ciphertext, tag)

# Print the decrypted message
print("Decrypted Message:", decrypted_message.decode())
