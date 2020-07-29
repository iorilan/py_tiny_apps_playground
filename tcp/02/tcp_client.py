from socket import *
import time, _thread 
import traceback

import helper 


host = '127.0.0.1'
port = 50008
sock = helper.tcp()
conn = sock.connect((host,port))
print('connected')

def listen_server():
    try:
        global sock
        while True:
            buff = sock.recv(1024)
            print(f'Client received: "{buff.decode()}"')
    except:
        traceback.print_exc()

_thread.start_new_thread(listen_server, ())

def listen_keyboard():
    while True:
        print('key in message :')
        msg = input()
        if msg.lower() == 'q':
            break
        
        byte_arr = msg.encode(encoding='utf-8')
        sock.send(byte_arr)
listen_keyboard()

sock.close()
print ("connection closed")