"""
a way to achieve multiple-inheritance (but not recommended)
will take first match 
"""
class Mixin1(object):
    def test(self):
        print ("Mixin1")

class Mixin2(object):
    def test(self):
        print ("Mixin2")

class MyClass(Mixin1, Mixin2):
    pass

if __name__ == "__main__":
    MyClass().test()

