import math

def RSA():
   p = 7
   q = 13
   n = p * q
   euler = (p - 1) * (q - 1)

   # 1<e<euler
   # find e
   def find_e(euler):
       for i in range(2, euler+1):
           if math.gcd(i, euler) == 1:
               return i

   e = find_e(euler)

   # find d
   def find_d(e, func):
       for i in range(0, 100):
           if (e * i) % func == 1:
               return i

   d = find_d(e, euler)

   plaintext = 7
   c = pow(plaintext, e) % n  # c = p^e * mod(n) - encrypted message
   m = pow(c, d) % n  # p = c^d * mod(n) - decrypted message

   print("plaintext is =", plaintext)
   print("p =", p)
   print("q =", q)
   print("n =", n)
   print("Euler =", euler)
   print("e key =", e)
   print("d key =", d)
   print("encrypted message is", c)
   print("decrypted message is", m)

RSA()
