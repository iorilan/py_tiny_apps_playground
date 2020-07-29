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
q=[] # messages 
clients=[] # array of connections 
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
                outputs.append(conn)
            else:
                try:
                    data_byte = s.recv(1024)
                    #client disconnected
                    if not data_byte:
                        inputs.remove(s)
                        clients.remove(s)
                        outputs.remove(s)
                        s.close()
                    else:
                        msg = data_byte.decode()
                        print(f'received: {msg}')
                        q.append(msg)
                except:
                    inputs.remove(s)
                    clients.remove(s)
                    outputs.remove(s)

        # broadcasting message to all socket connections
        while len(q) > 0:
            msg = q.pop(0)
            for w in writable:
                w.send(msg.encode())
                
_thread.start_new_thread(run,())

while True:
    print("press q to exit")
    if(input() == 'q'):
        _running = False
        break
