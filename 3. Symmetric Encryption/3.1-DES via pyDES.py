import pyDes # Importing libraries (pyDES)


data = “DES Algorithm” # Plaintext
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5) # Initializing DES object
d = k.encrypt(data) # Encrypting data using k object and stores it in d variable

print("Encrypted: %r" % d)
print("Decrypted: %r" % k.decrypt(d))
