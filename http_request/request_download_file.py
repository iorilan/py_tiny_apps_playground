"""
    get
"""
import requests

resp=requests.get("http://localhost:5001/get/file/hello.txt")
resp.raise_for_status()
temp_file = open("h.txt","wb")
for chunk in resp.iter_content(100000):
    temp_file.write(chunk)

temp_file.close()