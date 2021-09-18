import socket

# host = "192.168.0.157"
host = "127.0.0.1"
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while True:
        data = input("Enter message to send->> ").encode("utf-8")
        s.sendall(data)
        print("OVER!")
        data  = s.recv(1024)
        print("Message from server: ", data.decode("utf-8"))
