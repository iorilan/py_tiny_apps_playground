import ssh_client as sc
import os
import time

def run_cmd():
    session = sc.ssh_session()
    session.run("who").run("cd /").run("ls").logout()
    #session.run("mkdir folder1").logout()

def upload_sample():
    session = sc.ssh_session()
    
    session.upload(os.path.join("sample_data","upload.txt"),f"./uploaded/upload_{time.time()}.txt")
    session.logout()

def download_sample():
    session = sc.ssh_session()
    session.download("./download/1.txt", os.path.join("sample_data","download_1.txt"))

if __name__ == "__main__":
    run_cmd()
    #upload_sample()
    #download_sample()