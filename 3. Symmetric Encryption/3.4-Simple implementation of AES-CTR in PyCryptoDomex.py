from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

# Key (16 bytes for AES-128)
key = get_random_bytes(16)

# Nonce (must be unique for each encryption operation)
nonce = get_random_bytes(8)  # 64 bits for AES-CTR

# Create the AES cipher object in CTR mode
cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

# Input plaintext
plaintext = b'Hello, CTR mode!'

# Encrypt the plaintext
ciphertext = cipher.encrypt(plaintext)

# Decrypt the ciphertext
decipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
recovered_plaintext = decipher.decrypt(ciphertext)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext.hex())
