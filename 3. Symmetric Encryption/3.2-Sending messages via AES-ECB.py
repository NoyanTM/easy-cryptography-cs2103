# Importing json, cryptography libraries
import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Defining test_key and aesCipher
test_key = bytes.fromhex('00112233445566778899AABBCCDDEEFF')
aesCipher = Cipher(algorithms.AES(test_key), modes.ECB(), backend=default_backend())

def encrypt_message(message):
    message += b"E" * (-len(message) % 16)
    aesEncryptor = aesCipher.encryptor()
    ciphertext = aesEncryptor.update(message)
    return ciphertext.hex()

def decrypt_message(ciphertext):
    aesDecryptor = aesCipher.decryptor()
    recovered = aesDecryptor.update(bytes.fromhex(ciphertext))
    unpadded = recovered.rstrip(b"E")
    return unpadded.decode()

def save_message(filename, message):
    with open(filename, 'a') as f:
        f.write(json.dumps(message) + '\n')

def read_messages(filename, recipient):
    messages = []
    with open(filename, 'r') as f:
        for line in f:
            message = json.loads(line)
            if message['to'] == recipient:
                messages.append(message)

    return messages

def send_message(sender, recipient):
    message_text = input(f"{sender}, enter your message to {recipient}: ")
    ciphertext = encrypt_message(message_text.encode())
    message = {'from': sender, 'to': recipient, 'message': ciphertext}
    save_message('messages.json', message)
    print(f"Message from {sender} to {recipient} sent!")

def read_message(recipient):
    messages = read_messages('messages.json', recipient)
    if not messages:
        print(f"No messages for {recipient}!")
        return

    for message in messages:
        sender = message['from']
        ciphertext = message['message']
        plaintext = decrypt_message(ciphertext)
        print(f"Message from {sender}: {plaintext}")

while True:
    user = input("Enter your name (Alice / Bob): ")
    if user == 'Alice':
        action = input("Enter action (send / read / exit): ")
        if action == 'send':
            send_message('Alice', 'Bob')
        elif action == 'read':
            read_message('Alice')
        elif action == 'exit':
            break
        else:
            print("Invalid action!")
    elif user == 'Bob':
        action = input("Enter action (send / read / exit): ")
        if action == 'send':
            send_message('Bob', 'Alice')
        elif action == 'read':
            read_message('Bob')
        elif action == 'exit':
            break
        else:
            print("Invalid action!")
    else:
        print("Invalid user!")
