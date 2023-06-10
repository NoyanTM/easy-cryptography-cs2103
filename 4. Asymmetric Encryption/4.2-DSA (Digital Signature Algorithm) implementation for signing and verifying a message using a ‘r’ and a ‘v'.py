import random
import math

p = 17  # prime number
message = 6  # message

print('Prime number is:', p)
print('Message is:', message)

h = message % p  # hashed message
print('Hashed message is:', h)


# to find prime divisor
def prime_divisor(n):
   prime = -1
   while n % 2 == 0:
       prime = 2
       n = n / 2

   for i in range(3, int(math.sqrt(n)) + 1, 2):
       while n % i == 0:
           prime = i
           n = n // i
       if n > 1:
           prime = n
           return prime


# to find g
def g_find():
   for g in range(1, p):
       if ((pow(g, q) % p) == 1) or (g == (pow(h, (p - 1) / q)) % p):
           return g


# fo find inverse
def inverse(a, b):
   for i in range(0, 100):
       if (a * i) % b == 1:
           return i


# key generation
q = prime_divisor(p)  # prime divisor
x = random.randint(1, p - 1)  # random integer (private key)
g = g_find()
y = (g ** x) % p  # public key, y = g^x * mod(p)
print('Private key is:', p, q, g, x)
# signing process
k = random.randint(1, p - 1)  # random integer k
r = (pow(g, k) % p) % q  # r = (g^k * mod(p)) * mod(q)
k_inv = inverse(k, q)  # k^-1
s = (k_inv * (h + x * r)) % q
print('Signature is:', r, s)

# verification process
w = inverse(s, q)
u1 = (h * w) % q
u2 = (r * w) % q
v = ((pow(g, u1) * pow(y, u2)) % p) % q  # v = ((g^u1 * y^u2) mod p) mod q
print('r is:', r)
print('v is:', v)

if v == r:
   print('Verification successful')
else:
   print('Verification denied')
