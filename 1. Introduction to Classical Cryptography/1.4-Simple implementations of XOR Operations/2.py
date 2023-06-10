def XOR(x, y):

    x_bin = bin(x)[2:]
    y_bin = bin(y)[2:]

    length = max(len(x_bin), len(y_bin))
    x_bin = x_bin.zfill(length)
    y_bin = y_bin.zfill(length)

    res_bin = [str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(x_bin, y_bin)]
    res_dec = int(''.join(res_bin), 2)
    return res_bin, res_dec

x = int(input("Input 1st number:"))
y = int(input("Input 2nd number:"))
print(f"Result:", XOR(x, y))
