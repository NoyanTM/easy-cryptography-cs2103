def reverse_cipher(msg):
        reverse_msg = msg[::-1]
        return reverse_msg

msg = input("Enter your message to reverse: ")
print("Reversed message: ", reverse_cipher(msg))
