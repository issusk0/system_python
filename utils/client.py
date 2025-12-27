import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



host = socket.gethostname()

port = 8000


try:
    client_socket.connect((host, port))
    while True:
        
        data  = client_socket.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")
        client_socket.close()
except Exception as e:
    print(e)