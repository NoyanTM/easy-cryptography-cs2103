from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

# Key (16 bytes for AES-128)
key = get_random_bytes(16)

# Initialization Vector (IV)
iv = get_random_bytes(16)

# Create the AES cipher object in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Input plaintext (must be a multiple of the block size)
plaintext = b'Hello, CBC mode!'

# Encrypt the plaintext
ciphertext = cipher.encrypt(plaintext)

# Decrypt the ciphertext
decipher = AES.new(key, AES.MODE_CBC, iv)
recovered_plaintext = decipher.decrypt(ciphertext)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext.hex())
