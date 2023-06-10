import socket
import ssl

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with TLS using the ssl module
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
tls_sock = context.wrap_socket(sock, server_hostname='example.com')

# Connect to the server
tls_sock.connect(('example.com', 443))

# Send and receive data over the TLS connection
tls_sock.sendall(b'Hello, server!')
response = tls_sock.recv(1024)

# Close the TLS connection
tls_sock.close()
