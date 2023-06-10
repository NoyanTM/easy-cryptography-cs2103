import os
from cryptography.hazmat.primitives.ciphers.aead import AESCCM
data = b"a secret message"
aad= b"authenticated but unencrypted data"
key = AESCCM.generate_key(bit_lenght=128)
aesccm = AESCCM(key)
nonce = os.urandom(7)
ct = aesccm.encrypt(nonce, data, aad)
aesccm.decrypt(nonce, ct, aad)
