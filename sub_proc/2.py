import os, sys
import subprocess

proc=[]
while True:
    cmd = input().lower().split(' ')
    if cmd[0] == 'start':
        p = subprocess.Popen([sys.executable,'1.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
        print(f'process started: {p.pid}')
        """
            sudo ps -a -T |grep testing_py
        """
        proc.append(p)
    elif cmd[0] == 'kill':
        the_proc = [x for x in proc if x.pid == int(cmd[1])]
        if len(the_proc)>0:
            the_proc[0].terminate()
            print('killed!')


    