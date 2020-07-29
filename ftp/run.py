import ftp_client as fc
import os

ftp_test_url = 'ftp.dlptest.com'
_user_name = 'dlpuser@dlptest.com'
_pwd = 'SzMf7rTE4pCrf9dV286GuNe4N'
def dir():
    res = fc.folders(ftp_test_url,_user_name,_pwd)
    for r in res:
        print (r)

def upload():
    fc.upload(ftp_test_url,'sample_data/upload.txt',_user_name,_pwd )
    fc.upload(ftp_test_url,'sample_data/upload.obj',_user_name,_pwd )
    
def download():
    fc.download(ftp_test_url, "upload.obj",os.path.join("sample_data","dl_obj.obj"),_user_name, _pwd)
    fc.download(ftp_test_url, "upload.txt",os.path.join("sample_data","dl_obj.txt"),_user_name, _pwd)

if __name__ == "__main__":
    #dir()
    #upload()
    download()