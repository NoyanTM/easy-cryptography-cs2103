import hashlib

filename = 'Untitled-1.jpeg'

with open(filename, mode='rb') as f:
    md5 = hashlib.md5()
    data = f.read()
    md5.update(data)
md5sum = md5.hexdigest()

with open(filename, mode='rb') as f:
    sha256 = hashlib.sha256()
    data = f.read()
    sha256.update(data)
sha256sum = sha256.hexdigest()

print(f"MD5 sum of {filename}: {md5sum}")
print(f"SHA-256 sum of {filename}: {sha256sum}")
