import hashlib
import itertools

def crack_hash(hash_value, charset, max_length):
    for length in range(1, max_length + 1):
        for combination in itertools.product(charset, repeat=length):
            word = ''.join(combination)
            hashed_word = hashlib.md5(word.encode()).hexdigest()  # Desired hash algorithm

            if hashed_word == hash_value:
                return word  # Return the cracked password if a match is found

    return None  # Return None if no match is found

# Example usage
target_hash = "e2fc714c4727ee9395f324cd2e7f331f"  # Target hash value
charset = "abcdefghijklmnopqrstuvwxyz"  # Characters list for brute forcing
max_length = 4  # Maximum length of the password / plaintext

cracked_password = crack_hash(target_hash, charset, max_length)
if cracked_password:
    print("Password cracked:", cracked_password)
else:
    print("Password not found through brute force.")
