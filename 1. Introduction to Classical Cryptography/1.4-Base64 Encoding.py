import base64

# Base64 Encoding Example
message = "Hello, World!"

# Convert string to bytes
message_bytes = message.encode('utf-8')

# Encode bytes to Base64 representation
base64_representation = base64.b64encode(message_bytes)

# Convert Base64 bytes to string
base64_string = base64_representation.decode('utf-8')

print("Base64 Representation:", base64_string)
