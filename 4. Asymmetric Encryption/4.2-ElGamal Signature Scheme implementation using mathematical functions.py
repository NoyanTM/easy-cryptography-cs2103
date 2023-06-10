import random

# to find primitive root of prime number
def is_primitive_root(a, n):
   uniques = set()
   for i in range(1, n):
       unique = pow(a, i, n)
       uniques.add(unique)
   return len(uniques) == n - 1


def find_primitive_root(n):
   for a in range(2, n):
       if is_primitive_root(a, n):
           return a
   return None


# Alice's key generation
p = 17  # prime number
g = find_primitive_root(p)  # primitive root of prime number
a = random.randint(1, p - 1)  # random integer (private key) 1<a<p-1
e = g ** a % p
print('Prime number is:', p)
print('Primitive root is:', g)
print('Private key is:', a)
print("Alice's public key:", (p, g, e))

# Encryption (Bob - message sender)
m = 9  # plaintext, m<p
b = random.randint(1, p - 1)  # random integer
c_1 = g ** b % p  # C1 = g^b mod(p)
c_2 = m * pow(e, b) % p  # C2 = m * e^b mod(p)
print("Bob's plaintext is:", m)
print("Bob's ciphertext is:", (c_1, c_2))

# Decryption (Alice - message receiver)
x = pow(c_1, a) % p  # x = (C1)^a mod(p)
decrypted = c_2 * pow(x, p - 2) % p  # m = C2 * x^(p-2) mod(p)

print('Decrypted message is:', decrypted)
