import rsa

with open("public.pem", "rb") as f:
	public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
	private_key = rsa.PrivateKey.load_pkcs1(f.read())
message = "Astana IT University Random Password"

# encrypted_message = rsa.encrypt(message.encode(), public_key)
# with open("encrypted.message", "wb") as f:
# 	f.write(encrypted_message)

encrypted_message = open("encrypted.message", "rb").read()

clear_message = rsa.decrypt(encrypted_message, private_key)
print(clear_message.decode())


#import rsa

# Generate RSA key pair
#(public_key, private_key) = rsa.newkeys(2048)  # 2048 is the key size in bits

# Example plaintext
#message = b"Hello, RSA!"

# Encrypt using the public key
#ciphertext = rsa.encrypt(message, public_key)

# Decrypt using the private key
#decrypted_message = rsa.decrypt(ciphertext, private_key)

#print("Original message:", message)
#print("Decrypted message:", decrypted_message.decode())
