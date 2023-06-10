from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

# Generate ECC key pair
private_key = ec.generate_private_key(
    ec.SECP256R1(),  # Choosing the curve (SECP256R1 is a commonly used curve)
    default_backend()
)
public_key = private_key.public_key()

# Obtain the public key in bytes
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Sign a message using the private key
message = b"Hello, ECC!"
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

# Verify the signature using the public key
try:
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    print("Signature is valid.")
except InvalidSignature:
    print("Signature is invalid.")
