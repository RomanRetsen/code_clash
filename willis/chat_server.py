import socket
import select
import sys
import _thread


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip = "127.0.0.1"
port = 20000
server.bind((ip, port))
server.listen(100)
list_of_clients = []

def client_thread(conn, addr):
    conn.send(b"Welcome to the chat room")

    while True:
        try:
            message = conn.recv(2048)
            if message:
                message_to_send = "<" + addr[0] + ">" + message
                print(message_to_send)
                broadcast(message_to_send, conn)
            else:
                print("removing")
                remove_client(conn)
        except:
            continue

def broadcast(message, connection):
    for client in list_of_clients:
        if client != connection:
            try:
               client.send(message)
            except:
                client.close()
                remove_client(client)

def remove_client(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0], " got connected")
    _thread.start_new_thread(client_thread, (conn, addr))

conn.close()
server.close()


















