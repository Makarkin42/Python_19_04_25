import socket
import time

master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
master.bind(("localhost", 10524))
master.setblocking(False)
master.listen(5)
print("Сокет создан!")
users = {}

while True:
    time.sleep(1)
    try:
        clients, adress = master.accept()
        clients.setblocking(False)
        print(adress, "Подключился")
        users[adress] = clients
    except BlockingIOError:
        pass

    for i in users:
        try:
            users[i].send("Я тут".encode())
            mess = master.recv(1024).decode()
            print(mess)
        except(BlockingIOError, ConnectionResetError, ConnectionAbortedError):
            pass