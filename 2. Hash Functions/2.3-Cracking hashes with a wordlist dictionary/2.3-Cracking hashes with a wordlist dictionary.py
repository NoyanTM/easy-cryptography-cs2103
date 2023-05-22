import hashlib

def crack_hash(hash_value, wordlist_file):
    with open(wordlist_file, 'r') as file:
        for line in file:
            word = line.strip()
            hashed_word = hashlib.md5(word.encode()).hexdigest()  # Hash algorithm

            if hashed_word == hash_value:
                return word  # Return the cracked password if a match is found

    return None  # Return None if no match is found

# Example usage
target_hash = "e2fc714c4727ee9395f324cd2e7f331f"  # Target hash value
wordlist = "wordlist.txt"  # Path to your wordlist file

cracked_password = crack_hash(target_hash, wordlist)
if cracked_password:
    print("Password cracked:", cracked_password)
else:
    print("Password not found in the wordlist.")
