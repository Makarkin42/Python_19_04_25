import socket
import random
import time
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:4252@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Stats(Base):
    __tablename__ = "register_base"
    login = Column(String, primary_key=True)
    password = Column(String, nullable=False)

Base.metadata.create_all(engine)

#192.168.1.14
master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
master.bind(("192.168.1.15", 12516))
master.setblocking(False)
master.listen(5)

while True:
    time.sleep(1)
    try:
        clients, adres = master.accept()
        clients.setblocking(False)
        print(adres, "Подключился")
        mess = clients.recv(1024).decode()
        print(mess)
        login, password = mess.split(",")
        user = session.get(Stats, login)
        print(user)
        if user is not None:
            if user.password == password:
                print(True)
                clients.send("<1>".encode())
            else:
                print(False)
                clients.send("<-1>".encode())
        else:
            print("Такой логин не зарегестрирован!")
            clients.send("<0>".encode())
    except BlockingIOError:
        pass