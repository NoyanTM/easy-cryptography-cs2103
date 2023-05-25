# Example 2. NIST KATs of AES-ECB
import re
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Reading .rsp file
file_name = input('Enter file name: ')
with open(file_name, "r") as f:
    data = f.read()

# Splitting file into encryption / decryption sections
sections = re.split(r'\[ENCRYPT\]|\[DECRYPT\]', data)[1:]

def parse_section(section):
    # Splitting section into individual test cases
    test_cases = re.findall(r'COUNT = \d+\nKEY = [0-9a-fA-F]+\nPLAINTEXT = [0-9a-fA-F]+\nCIPHERTEXT = [0-9a-fA-F]+\n', section)
    
    # Initializing list to store plaintext and ciphertext pairs
    pairs = []
    
    # Looping through test cases and parse required data
    for test_case in test_cases:
        plaintext = re.search(r'PLAINTEXT = ([0-9a-fA-F]+)\n', test_case).group(1)
        ciphertext = re.search(r'CIPHERTEXT = ([0-9a-fA-F]+)\n', test_case).group(1)

        # Appending plaintext and ciphertext pair to list
        pairs.append((plaintext, ciphertext))

    # Returning list of plaintext and ciphertext pairs
    return pairs

# Initializing empty list to store all plaintext and ciphertext pairs
nist_kats = []

# Looping through encryption / decryption sections and parse data
for section in sections:
    # Parsing plaintext and ciphertext pairs for section
    pairs = parse_section(section)
    
    # Adding pairs to nist_kats list
    nist_kats.extend(pairs)
    
# Defining test key
key = re.search(r'KEY = ([0-9a-fA-F]+)\n', data).group(1)
test_key = bytes.fromhex(key)

# Debugging keys, ciphertexts, plaintexts
print(nist_kats)
print(test_key)

# AESCipher for ECB
aesCipher = Cipher(algorithms.AES(test_key), modes.ECB(), backend=default_backend())
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

# Testing each input
for index, kat in enumerate(nist_kats):
        plaintext, want_ciphertext= kat
        plaintext_bytes = bytes.fromhex(plaintext)
        ciphertext_bytes = aesEncryptor.update(plaintext_bytes)
        got_ciphertext = ciphertext_bytes.hex()
        result = "[PASS]" if got_ciphertext == want_ciphertext else "[FAIL]"
        print("Test {}. Expected {}, Got {}. Result {}.".format(index, want_ciphertext, got_ciphertext, result))
