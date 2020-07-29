from socket import *
import datetime
import helper

host = '127.0.0.1'
port = 50008

sock = helper.tcp()

sock.bind((host,port))
sock.listen()

while True:
    
    conn,addr = sock.accept()
    print(f'new connection :{addr}')
    while True:
        data = conn.recv(1024)
        msg = data.decode()
        # this is the signal sent from client to indicate connection closed
        if not data: break 
        print(f'received : {msg}')
        echo_byte = f'{datetime.datetime.now()} server received : "{msg}"'.encode()
        conn.send(echo_byte)
    conn.close()
    print ('connection closed')