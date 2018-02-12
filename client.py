import socket
import threading
import time
import updater

shutdown = False


def getmsg(name, s):
    while not shutdown:
        try:
            while True:
                msg = s.recv(1024).decode()
                msg = str(msg)
                if not msg:
                    pass
                else:
                    print("\nReceived from server: " + msg)
        except:
            time.sleep(1)


host = input("Enter server ip: ")
port = int(input("Enter server port: "))

s = socket.socket()
s.connect((host, port))
s.setblocking(0)

rT = threading.Thread(target=getmsg, args=("name", s))
rT.start()

message = input(">> ")
while message != "q":
    if message == "/update":
        updater.update()
    else:
        s.send(message.encode())
        message = input()
shutdown = True
rT.join()
s.close()
