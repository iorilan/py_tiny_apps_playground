from socket import *
import datetime
import time, _thread 
import helper
import traceback

host = '127.0.0.1'
port = 50008

sock = helper.tcp()

sock.bind((host,port))
sock.listen()

clients = {}
_running = True
def new_client(conn):
    global _running

    clients[str(conn)] = conn
    while _running:
        buf=None
        try:
            buf = conn.recv(1024)
        except:
            print("client disconnected.")

        if not buf:
            try:
                del clients[str(conn)]
            except:
                print("failed to remove client")

            print(f'# of connections : {len(clients)}')
        else:
            s = buf.decode()

            print(f'received from client : {s}')
            msg = f'Echo : {time.time()}'.encode()

            for c in clients.values():
                c.send(msg)


def forever_run():
    global _running
    while _running:
        conn,addr = sock.accept()
        print(f'[{datetime.datetime.now()}]: new connection :{addr}')
        # print(conn.getsockname())
        # print(conn.getpeername())
        # print(str(conn))
        _thread.start_new_thread(new_client, (conn,))

_thread.start_new_thread(forever_run,())

while True:
    msg = input()
    if msg == 'q':
        _running = False
        break



