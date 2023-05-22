import hashlib
import os

def generate_salt(length=16):
    return os.urandom(length)

def calculate_hash(data):
    hash_object = hashlib.sha256(data.encode('utf-8'))
    hash_value = hash_object.hexdigest()
    return hash_value

def calculate_hash_with_salt(data, salt):
    salted_data = salt + data.encode('utf-8')
    hash_object = hashlib.sha256(salted_data)
    hash_value = hash_object.hexdigest()
    return hash_value

# Example usage
password = "my-password"

# Generate a random salt
salt = generate_salt()

# Calculate normal SHA-256 hash
normal_hashed_password = calculate_hash(password)
print("Normal Hashed Password:", normal_hashed_password)

# Calculate salted SHA-256 hash
salted_hashed_password = calculate_hash_with_salt(password, salt)
print("Salted Hashed Password:", salted_hashed_password)
