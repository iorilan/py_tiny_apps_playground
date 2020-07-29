import ftplib
import os

def folders(url, username, password, cwd=None):
    ftp = ftplib.FTP(url)
    ftp.login(username,password)

    res = []
    if cwd:
        ftp.cwd(cwd)
    ftp.dir(res.append)

    ftp.quit()

    return res

def upload(url, file_name, username, password,cwd=None):
    print(f"uploading {file_name}...")
    ftp = ftplib.FTP(url)
    ftp.login(username, password)
    if cwd:
        ftp.cwd(cwd)
    ext = file_name.split('.')[-1]
    name = os.path.basename(file_name)
    print(f'base name : {name}')
    if ext in ['txt','html'] :
        ftp.storlines("STOR "+name, open(file_name,'rb'))
    else:
        ftp.storbinary("STOR "+name, open(file_name, 'rb'), 1024)

    ftp.quit()

def download(url, filename, to_file, username, password, cwd =None):
    print(f'downloading {filename}...')
    
    ftp = ftplib.FTP(url)
    ftp.login(username, password)
    if cwd:
        ftp.cwd(cwd)
    try:
        ftp.retrbinary("RETR "+filename, open(to_file,'wb').write)
    except : print("Error")

    ftp.quit()