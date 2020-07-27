import re

class regEx:
    def zeroOrOne(s,c ):
        p = re.compile(f'{c}?')
        return p.search(s) != None
    
    def zeroOrMore(s,c):
        p = re.compile(f'{c}+')
        return p.search(s) != None

    def oneOrMore(s,c):
        p = re.compile(f'{c}?')
        return p.search(s) != None

    def ndigit(s,n):
        p = re.compile(r'\d{n}')
        return p.search(s) != None

    def nOrMoredigit(s,n):
        p = re.compile(r'\d{n,}')
        return p.search(s) != None

    def zeroToMdigit(s,m):
        p = re.compile(r'\d{,m}')
        return p.search(s) != None

    def nToMoredigit(s,n,m):
        p = re.compile(r'\d{n,m}')
        return p.search(s) != None

    def startWith(s, p):
        p = re.compile(f'^{p}')
        return p.search(s) != None

    def endWith(s, p):
        p = re.compile(r'{p}$')
        return p.search(s) != None

    def hasDigit(s,p):
        p = re.compile(r'\d')
        return p.search(s) != None

    def anythingExceptDigit(s,p):
        p = re.compile(r'\D')
        return p.search(s) != None

    def hasWord(s,p):
        p = re.compile(r'\w')
        return p.search(s) != None

    def anythingExceptWord(s,p):
        p = re.compile(r'\W')
        return p.search(s) != None

    def hasSpace(s,p):
        p = re.compile(r'\s')
        return p.search(s) != None

    def anythingExceptSpace(s,p):
        p = re.compile(r'\S')
        return p.search(s) != None

    def hasAny(s,p):
        p = re.compile(f'[{p}]')
        return p.search(s) != None

    def notHasAny(s,p):
        p = re.compile(f'[^{p}]')
        return p.search(s) != None