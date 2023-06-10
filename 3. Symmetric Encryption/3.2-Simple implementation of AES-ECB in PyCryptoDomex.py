from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Key (16 bytes for AES-128)
key = get_random_bytes(16)

# Create the AES cipher object in ECB mode
cipher = AES.new(key, AES.MODE_ECB)

# Input plaintext (must be a multiple of the block size)
plaintext = b'Hello, ECB mode!'

# Encrypt the plaintext
ciphertext = cipher.encrypt(plaintext)

# Decrypt the ciphertext
recovered_plaintext = cipher.decrypt(ciphertext)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext.hex())
