""" selector of bs4:
soup.select('div')                      All elements named <div>
soup.select('#author')                  The element with an id attribute of author
soup.select('.notice')                  All elements that use a CSS class attribute named notice
soup.select('div span')                 All elements named <span> that are within an element named <div>
soup.select('div > span')               All elements named <span> that aredirectly within an element named <div>,with no other element in between
soup.select('input[name]')              All elements named <input> that have a name attribute with any value
soup.select('input[type="button"]')     All elements named <input> that have an attribute named type with value button

more details
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#calling-a-tag-is-like-calling-find-all
"""