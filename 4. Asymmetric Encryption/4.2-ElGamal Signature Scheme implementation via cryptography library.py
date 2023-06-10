from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

# Generate an EC private key for ElGamal
private_key = ec.generate_private_key(
    ec.SECP256R1(), default_backend()
)

# Get the corresponding public key
public_key = private_key.public_key()

# Message to be signed
message = b"Hello, World!"

# Sign the message using ElGamal
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

# Verify the signature
try:
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    print("Signature is valid.")
except InvalidSignature:
    print("Signature is invalid.")
