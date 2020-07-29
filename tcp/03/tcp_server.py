from socket import *
import datetime,time,_thread
from select import select
import helper
import traceback

host = '127.0.0.1'
port = 50018

server = helper.tcp()
#server.setblocking(0)
server.bind((host,port))
server.listen(5)
inputs,outputs,[] = [server],[],[]
clients=[]
_running = True

def run():
    global _running
    while _running:
        readable, writable, exp = select(inputs, outputs, [])
        for s in readable:
            if s is server:
                conn,addr = s.accept()
                #conn.setblocking(0)
                print(f'[time.time()] new connection: {addr}')
                inputs.append(conn)
                clients.append(conn)
            else:
                try:
                    data_byte = s.recv(1024)
                    #client disconnected
                    if not data_byte:
                        s.close()
                        inputs.remove(s)
                        clients.remove(s)
                    else:
                        msg = data_byte.decode()
                        print(f'received: {msg}')
                        for r in clients:
                            r.send(f'From Server: {time.time()}'.encode())
                except:
                    inputs.remove(s)
                    clients.remove(s)
                    
_thread.start_new_thread(run,())

while True:
    print("press q to exit")
    if(input() == 'q'):
        _running = False
        break
