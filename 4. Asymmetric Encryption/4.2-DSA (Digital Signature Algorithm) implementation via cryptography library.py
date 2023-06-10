from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend

# Generate a DSA private key
private_key = dsa.generate_private_key(
    key_size=1024, backend=default_backend()
)

# Generate the corresponding public key
public_key = private_key.public_key()

# Message to be signed
message = b"Hello, World!"

# Generate the digital signature
signature = private_key.sign(
    message, hashes.SHA256()
)

# Verify the digital signature
try:
    public_key.verify(signature, message, hashes.SHA256())
    print("Signature is valid.")
except InvalidSignature:
    print("Signature is invalid.")
