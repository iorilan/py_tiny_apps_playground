"""
extract all one piece link and name
http://fanfox.net/manga/one_piece/
"""

import requests, bs4


headers = {'User-Agent': 'Mozilla/5.0'}
res = requests.get('http://fanfox.net/manga/one_piece/',
headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.content,'lxml')

items = soup.find(id="list-2").find_all("a", limit=5)
arr = [{'name':a.attrs['title'],'link':a.attrs['href']} for a in items]
for a in arr:
    for k,v in a.items():
        print(f'{k}:{v}', end='|')
    print("==")
