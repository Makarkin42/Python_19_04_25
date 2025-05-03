import socket

master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
master.connect(("localhost", 10524))
users = {}

while True:
    try:
        mess = master.recv(1024).decode()
        print(mess)
        for i in users:
            try:
                users[i].send("Я тут".encode())
            except(BlockingIOError, ConnectionResetError, ConnectionAbortedError):
                pass
    except(BlockingIOError, ConnectionResetError, ConnectionAbortedError):
        #print("800fps")
        pass