#import hashlib
#print(hashlib.algorithms_guaranteed) # Supported hash algorithms
#{'sha3_224', 'sha512', 'shake_128', 'md5', 'sha256', 'sha224', 'sha3_512', 'sha384', 'sha1', 'blake2s', 'shake_256', 'sha3_256', 'blake2b', 'sha3_384'}

import hashlib
hash_object = hashlib.new('algorithm_name') # Hash object using the desired algorithm
string = input() 
hash_object.update(string.encode('utf-8')) # Updating hash object with input string
hash_value = hash_object.hexdigest() # Retrieving the hash value
