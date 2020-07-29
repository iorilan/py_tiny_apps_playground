from socket import *
import datetime
import helper

host = '127.0.0.1'
port = 50007

sock = helper.udp()

sock.bind((host,port))

while True:
    msg,addr = sock.recvfrom(1024)
    print(f'[{datetime.datetime.now()}]: msg: {msg.decode()}, addr:{addr}')
    # this is the signal sent from client to indicate connection closed
    
    msg_server = f'{datetime.datetime.now()}: from server'.encode()
    sock.sendto(msg_server, addr)