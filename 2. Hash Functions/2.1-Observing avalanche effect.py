import hashlib

def different_bits(str1, str2):
        hash1 = hashlib.md5(str1.encode()).hexdigest()
        hash2 = hashlib.md5(str2.encode()).hexdigest()
        
        # Turning hashes to binary format
        bin1 = bin(int(hash1, 16))[2:].zfill(256)
        bin2 = bin(int(hash2, 16))[2:].zfill(256)

        diff = 0

        for i in range(len(bin1)):
                if bin1[i] != bin2[i]:
                        diff += 1
        return diff


# Printing number of different bits dependent on input data
str1 = input('Enter first string: ')
str2 = input('Enter second string: ')
print("Number of different bits: ", different_bits(str1, str2))
