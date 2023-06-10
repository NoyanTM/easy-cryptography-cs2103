import sympy

# ciphertext, e, and n are given for hacking RSA
e = 5
n = 91
encrypted_message = 63
print('n is', n)
print('e is', e)
print('encrypted message is', encrypted_message)

# factorize n into prime factors
factors = sympy.factorint(n)

# extract p and q from the factors
p = min(factors.keys())
q = n // p

print('p is', p)
print('q is', q)

euler = (p - 1) * (q - 1)
print('euler is', euler)


def find_d(e, func):
   for i in range(0, 100):
       if (e * i) % func == 1:
           return i


d = find_d(e, euler)
print('d is', d)

m = pow(encrypted_message, d) % n  # plaintext
print('plaintext is', m)
