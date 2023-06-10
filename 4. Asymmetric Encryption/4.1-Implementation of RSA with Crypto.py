from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

def rsa_encrypt(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message)
    return ciphertext

def rsa_decrypt(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    message = cipher.decrypt(ciphertext)
    return message

# Key generation (optional)
key = RSA.generate(2048)

# Export public and private keys to files (optional)
public_key = key.publickey()
private_key = key
public_key_export = public_key.export_key()
private_key_export = private_key.export_key()
with open('public_key.pem', 'wb') as file:
    file.write(public_key_export)
with open('private_key.pem', 'wb') as file:
    file.write(private_key_export)

# Load public and private keys from files
with open('public_key.pem', 'rb') as file:
    public_key = RSA.import_key(file.read())
with open('private_key.pem', 'rb') as file:
    private_key = RSA.import_key(file.read())

# Example usage
message = b'This is a secret message.'
ciphertext = rsa_encrypt(message, public_key)
decrypted_message = rsa_decrypt(ciphertext, private_key)

print("Original message:", message)
print("Decrypted message:", decrypted_message)
