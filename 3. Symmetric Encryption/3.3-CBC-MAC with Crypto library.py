from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def cbc_mac(key, message):
    key = pad(key, 16)[:16]  # Pad or truncate the key to 16 bytes
    cipher = AES.new(key, AES.MODE_CBC, IV=b'\x00' * 16)  # IV is set to all ze>
    ciphertext = cipher.encrypt(pad(message, 16))
    mac = ciphertext[-16:]  # Last 16 bytes as MAC
    return mac

# Example usage
key = b'SharedSecretKey'
message = b'This is the message to authenticate.'

mac = cbc_mac(key, message)
print("MAC:", mac.hex())
