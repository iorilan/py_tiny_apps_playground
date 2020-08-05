"""
sudo apt-get install build-essential libcap-dev
pip3 install python-prctl
nohup python3 1.py &
"""

import time 
import prctl
if __name__ == "__main__":
    prctl.set_name("testing_py")
    while(True):
        print('forever run')
        time.sleep(1)
    