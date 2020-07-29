#pip install paramiko
import paramiko
from paramiko import SSHClient


class ssh_session:
    def __init__(self):
        _username="newstart"
        _password="123456"
        vm_ip = "192.168.11.137"
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(vm_ip, 22, username=_username, password=_password)

    def run(self, cmd):
        stdin, stdout, err = self.client.exec_command(cmd)
        print(stdout.readline(2048))
        return self

    def upload(self, from_path, file):
        sftp=self.client.open_sftp()
        sftp.put(from_path, file)
        print(f'file uploaded.')
        #self.run(f"mv {file} ./uploaded")
        #print("filed moved")
        

    def download(self, from_path, to_path):
        sftp=self.client.open_sftp()
        sftp.get(from_path, to_path)
        print(f'file downloaded.')

    def logout(self):
        self.client.close()

