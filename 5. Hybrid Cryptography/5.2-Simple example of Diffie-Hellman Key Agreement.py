# prime numbers
# p1*mod(p2)
print('prime1*mod(prime2)' + ' Input numbers into formula')
p1 = int(input('prime 1: '))
p2 = int(input('prime 2: '))

# private keys for Alice and Bob
Alice_key = int(input("ALice key: "))
Bob_key = int(input("Bob key: "))

# public values of Alice and Bob
alice = pow(p1, Alice_key) % p2  # p1^Alice_key mod(p2)
bob = pow(p1, Bob_key) % p2  # p1^Bob_key mod(p2)

# same keys for Alice and Bob
print('Keys for Alice and Bob: ')
print(pow(bob, Alice_key) % p2)  # Alice
print(pow(alice, Bob_key) % p2)  # Bob
