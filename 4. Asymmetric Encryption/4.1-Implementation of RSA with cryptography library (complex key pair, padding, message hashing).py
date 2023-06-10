from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_keypair():
   # Generate a key pair
   private_key = rsa.generate_private_key(
   	public_exponent=65537,
   	key_size=2048
   )
   public_key = private_key.public_key()

   # Convert keys to byte format
   private_key_bytes = private_key.private_bytes(
   	encoding=serialization.Encoding.PEM,
   	format=serialization.PrivateFormat.PKCS8,
   	encryption_algorithm=serialization.NoEncryption()
   )
   public_key_bytes = public_key.public_bytes(
   	encoding=serialization.Encoding.PEM,
   	format=serialization.PublicFormat.SubjectPublicKeyInfo
   )

   # Return the public and private keys in byte format
   return public_key_bytes, private_key_bytes

def encrypt(public_key, message):
   # Load the public key
   public_key = serialization.load_pem_public_key(public_key)

   # Encrypt the message
   encrypted_message = public_key.encrypt(
   	message.encode('utf-8'),
   	padding.OAEP(
       	mgf=padding.MGF1(algorithm=hashes.SHA256()),
       	algorithm=hashes.SHA256(),
       	label=None
   	)
   )

   # Return the encrypted message
   return encrypted_message

def decrypt(private_key, encrypted_message):
   # Load the private key
   private_key = serialization.load_pem_private_key(private_key, password=None)

   # Decrypt the message
   decrypted_message = private_key.decrypt(
   	encrypted_message,
   	padding.OAEP(
       	mgf=padding.MGF1(algorithm=hashes.SHA256()),
       	algorithm=hashes.SHA256(),
       	label=None
   	)
   )

   # Return the decrypted message
   return decrypted_message.decode('utf-8')

# Example usage

# Generate keys
public_key, private_key = generate_keypair()
print("Public Key:\n", public_key.decode('utf-8'))
print("Private Key:\n", private_key.decode('utf-8'))

# Message to encrypt
message = "Hello, world!"

# Encrypt the message
encrypted_message = encrypt(public_key, message)
print("Encrypted Message:\n", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(private_key, encrypted_message)
print("Decrypted Message:\n", decrypted_message)
