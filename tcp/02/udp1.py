from socket import *
import datetime
import helper
import time,_thread

host = '127.0.0.1'

_running = True
def udp_listen():
    global _running

    port_listen = 50011
    sock = helper.udp()
    sock.bind((host,port_listen))

    while _running:
        msg,addr = sock.recvfrom(1024)
        print(f'[port: {port_listen}]: msg: {msg.decode()}, addr:{addr}')
        
_thread.start_new_thread(udp_listen, ())

def keyboard_listen():
    global _running

    send_to = ('127.0.0.1',50012)
    sock = helper.udp()

    while _running:
        print("send anything to udp client . press 'q' to exit. ")
        msg = input()
        if msg.lower() == 'q':
            _running = False
            break
        
        msg_bytes = msg.encode()
        sock.sendto(msg_bytes, send_to)

keyboard_listen()