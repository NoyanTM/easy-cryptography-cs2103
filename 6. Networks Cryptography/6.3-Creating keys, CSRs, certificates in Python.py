from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import datetime

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Create a Certificate Signing Request (CSR)
csr_builder = x509.CertificateSigningRequestBuilder()
csr_builder = csr_builder.subject_name(x509.Name([
    x509.NameAttribute(x509.NameOID.COMMON_NAME, 'example.com')
]))
csr_builder = csr_builder.add_extension(
    x509.BasicConstraints(ca=False, path_length=None),
    critical=True
)
csr = csr_builder.sign(private_key, hashes.SHA256(), default_backend())

# Generate a self-signed certificate
subject = issuer = x509.Name([
    x509.NameAttribute(x509.NameOID.COMMON_NAME, 'example.com')
])
cert_builder = x509.CertificateBuilder()
cert_builder = cert_builder.subject_name(subject)
cert_builder = cert_builder.issuer_name(issuer)
cert_builder = cert_builder.public_key(private_key.public_key())
cert_builder = cert_builder.serial_number(x509.random_serial_number())
cert_builder = cert_builder.not_valid_before(datetime.datetime.utcnow())
cert_builder = cert_builder.not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
cert_builder = cert_builder.add_extension(
    x509.BasicConstraints(ca=True, path_length=None), critical=True
)
cert_builder = cert_builder.add_extension(
    x509.SubjectAlternativeName([x509.DNSName('example.com')]), critical=False
)
certificate = cert_builder.sign(private_key, hashes.SHA256(), default_backend())

# Serialize private key
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
with open('private_key.pem', 'wb') as f:
    f.write(private_key_pem)

# Serialize CSR
csr_pem = csr.public_bytes(encoding=serialization.Encoding.PEM)
with open('csr.pem', 'wb') as f:
    f.write(csr_pem)

# Serialize certificate
certificate_pem = certificate.public_bytes(encoding=serialization.Encoding.PEM)
with open('certificate.pem', 'wb') as f:
    f.write(certificate_pem)
