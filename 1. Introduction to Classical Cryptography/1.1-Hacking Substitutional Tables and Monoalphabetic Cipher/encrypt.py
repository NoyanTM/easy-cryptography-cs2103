from string import ascii_letters, digits
from random import shuffle

def random_monoalpha_cipher(pool=None):
    if pool is None:
        pool = ascii_letters + digits
    original_pool = list(pool)
    shuffled_pool = list(pool)
    shuffle(shuffled_pool)
    return dict(zip(original_pool, shuffled_pool))

def inverse_monoalpha_cipher(monoalpha_cipher):
    inverse_monoalpha = {}
    for key, value in monoalpha_cipher.items():
        inverse_monoalpha[value] = key
    return inverse_monoalpha

def encrypt_with_monoalpha(message, monoalpha_cipher):
    encrypted_message = []
    for letter in message:
        encrypted_message.append(monoalpha_cipher.get(letter, letter))
    return ''.join(encrypted_message)

def decrypt_with_monoalpha(encrypted_message, monoalpha_cipher):
    return encrypt_with_monoalpha(
        encrypted_message,
        inverse_monoalpha_cipher(monoalpha_cipher)
    )

cipher = random_monoalpha_cipher()
print(cipher)
encrypted = encrypt_with_monoalpha('Hello all you hackers out there!', cipher)
decrypted = decrypt_with_monoalpha('sXGGt SGG Nt0 HSrLXFC t0U UHXFX!', cipher)

print(encrypted)
print(decrypted)
