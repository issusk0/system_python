import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = socket.gethostname()
port = 8000





server_socket.bind((addr, port))


server_socket.listen(5)


while True:
    clientsocket, addr = server_socket.accept()
    
    print(f"Got a connection from {addr}")
    
    # Send a message to the client (must be encoded to bytes)
    message = b'Thank you for connecting'
    clientsocket.send(message)
    
    # Close the connection with the client
    clientsocket.close()