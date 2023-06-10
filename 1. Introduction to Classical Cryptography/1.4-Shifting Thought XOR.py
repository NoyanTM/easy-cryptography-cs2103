# Define the messages to XOR
message1 = input("Enter msg1:")
message2 = input("Enter msg2:")

# Convert the messages to binary
binary1 = ''.join(format(ord(char), '08b') for char in message1)
binary2 = ''.join(format(ord(char), '08b') for char in message2)

# XOR the binary messages
xored = int(binary1, 2) ^ int(binary2, 2)

# Convert the XOR result back to binary and then to ASCII
result = bin(xored)[2:]
result = (8 - len(result) % 8) * '0' + result  # Pad the result with leading 0s if necessary
output = ''.join(chr(int(result[i:i+8], 2)) for i in range(0, len(result), 8))

print(output)
