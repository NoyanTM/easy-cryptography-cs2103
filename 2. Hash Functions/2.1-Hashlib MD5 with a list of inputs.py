import hashlib

inp = [b'alice', b'bob', b'balice', b'cob', b'a', b'aa', b'aaaaaaaaaa', b'a'*100000]

for i, inp in enumerate(inp):
    hash = hashlib.md5(inp).hexdigest()
    print(f"MD5 Hash of '{i+1}': {hash}")
