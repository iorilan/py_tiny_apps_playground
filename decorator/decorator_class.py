"""
    append attribute to class
"""

import uuid

def add_id(cls):
    init = cls.__init__

    def my_init(self, *args, **kwargs):
        self.id = uuid.uuid1()
        init(self, *args, **kwargs)
    cls.__init__ = my_init
    return cls

@add_id
class person:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f'{self.id},{self.name}'

def test_add_id():
    p = person('jeo')
    print(p)


if __name__ == "__main__":
    test_add_id()