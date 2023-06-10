import hashlib

def calculate_hash(data):
   hash_object = hashlib.sha256()
   hash_object.update(data.encode('utf-8'))
   return hash_object.hexdigest()

def verify_data_integrity(data, expected_hash):
   calculated_hash = calculate_hash(data)
   if calculated_hash == expected_hash:
       print("Data integrity verified. The data has not been altered.")
   else:
       print("Data integrity compromised. The data has been altered.")

# Usage example
original_data = "Hello, World!"
expected_hash = "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"

# Verify data integrity
verify_data_integrity(original_data, expected_hash)

# Modify the data
modified_data = "Hello, AITU!"

# Verify modified data integrity
verify_data_integrity(modified_data, expected_hash)
