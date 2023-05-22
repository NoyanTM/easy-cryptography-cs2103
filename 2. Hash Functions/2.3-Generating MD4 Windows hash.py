from Crypto.Hash import MD4 # pip install pycryptodome
text = 'p@ssw0rd'
hash_object = MD4.new(text.encode('utf-16le'))
digest = hash_object.hexdigest()
print(digest)
