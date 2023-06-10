import hashlib, hmac

def calculate_sha256_hash(data):
    hash_object = hashlib.sha256(data.encode())
    hash_value = hash_object.hexdigest()
    return hash_value

def calculate_hmac_sha256(key, data):
    hmac_object = hmac.new(key.encode(), data.encode(), hashlib.sha256)
    hmac_value = hmac_object.hexdigest()
    return hmac_value

# Example usage
key = "my-secret-key"
message = "Hello, world!"

# Calculate simple SHA-256 hash
sha256_hash = calculate_sha256_hash(message)
print("SHA-256 Hash:", sha256_hash)

# Calculate HMAC-SHA256
hmac_sha256 = calculate_hmac_sha256(key, message)
print("HMAC-SHA256:", hmac_sha256)
