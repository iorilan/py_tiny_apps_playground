from socket import *

def tcp():
    return socket(AF_INET, SOCK_STREAM)
    
def udp():
    return socket(AF_INET, SOCK_DGRAM)