# Binary Data and Logical Operators Example
binary_data_1 = b'\x01\x02\x03'  # bytes object
binary_data_2 = b'\x02\x03\x04'  # bytes object

# Bitwise AND
result_and = bytes([a & b for a, b in zip(binary_data_1, binary_data_2)])
print("Bitwise AND:", result_and)

# Bitwise OR
result_or = bytes([a | b for a, b in zip(binary_data_1, binary_data_2)])
print("Bitwise OR:", result_or)

# Bitwise XOR
result_xor = bytes([a ^ b for a, b in zip(binary_data_1, binary_data_2)])
print("Bitwise XOR:", result_xor)

# Bitwise NOT
result_not = bytes([255 - a for a in binary_data_1]) # result_not = bytes([~a for a in binary_data_1])
print("Bitwise NOT:", result_not)

# Bitwise Left Shift
result_left_shift = bytes([a << 1 for a in binary_data_1])
print("Bitwise Left Shift:", result_left_shift)

# Bitwise Right Shift
result_right_shift = bytes([a >> 1 for a in binary_data_1])
print("Bitwise Right Shift:", result_right_shift)
