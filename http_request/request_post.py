"""
    post json obj
"""

import requests

obj = {"abc":123,"cde":"456","def":{"aaa":"bbb"}}
params = {"key1":"v1","k2":2}
requests.post("http://localhost:5001/post/json", json=obj, params = params)