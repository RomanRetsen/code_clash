import socket


host = "127.0.0.1"
# host = "192.168.0.157"
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            str_data = data.decode("utf-8")
            if str_data == "exit":
                break
            print("Client said->> ", str_data)
            conn.sendall(input("Enter message to respond to client->> ").encode("utf-8"))