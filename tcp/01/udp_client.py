from socket import *
import helper 
host = ('127.0.0.1',50007)


while True:
    sock = helper.udp()
    print('key in message :')
    msg = input()
    if msg.lower() == 'q': 
        break
    bytes_arr = msg.encode()
    sock.sendto(bytes_arr, host)
    bytes_from_server,addr_server = sock.recvfrom(1024)
    print(f'Client received: "{bytes_from_server.decode()}"')