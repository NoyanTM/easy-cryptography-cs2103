import hashlib

md5_hash = hashlib.md5()
md5_hash.update(b'Trying to test ')
md5_hash.update(b'md5 hashing with update')
print('First output: ', md5_hash.hexdigest())

test = hashlib.md5(b'Trying to test md5 hashing with update')
print('Second output: ', test.hexdigest())
