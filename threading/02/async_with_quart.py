"""
pip install quart
"""

import asyncio
from quart import Quart

async def async_work(n):
    total = int(n)
    fab=[1,1]
    for i in range(1,total):
        fab.append(fab[-1]+fab[-2])
    
    return fab[-1]

app = Quart(__name__)

@app.route("/<n>")
async def calc(n):
    res=await async_work(n)
    return f'result: {res}'

if __name__ == "__main__":
    app.run(debug=False, port=50100)