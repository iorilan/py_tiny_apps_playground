"""
    post file with json obj
"""

import requests
import json

filename = 'sample.txt'
jsonobj = {'this':'is','a':{'sample':{'json':'obj'}}}
data = [
    ('upload_file', (filename, open(filename, 'rb'), 'application/octet')),
    ('json_data', ('data', json.dumps(jsonobj), 'application/json')),
]

headers = {'Authorization': 'my-api-key'}

requests.post("http://localhost:5001/post/file", headers=headers, files=data)
