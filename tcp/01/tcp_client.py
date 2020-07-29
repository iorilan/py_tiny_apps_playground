from socket import *
import helper 
host = '127.0.0.1'
port = 50008


while True:
    sock = helper.tcp()
    print('key in message :')
    msg = input()
    if msg.lower() == 'q': 
        break
    
    conn = sock.connect((host,port))
    byte_arr = msg.encode(encoding='utf-8')
    sock.send(byte_arr)
    
    buff = sock.recv(1024)
    print(f'Client received: "{buff.decode()}"')
    sock.close()
    print ("connection closed")