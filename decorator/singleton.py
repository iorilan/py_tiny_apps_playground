import functools

def singleton(cls):
    instance = {}
    def get_instance(*arg, **kwarg):
        if cls not in instance:
            instance[cls]=cls(*arg, **kwarg)
        return instance[cls]
    return get_instance

@singleton
class person:
    """ 
        since it is singleton 
        only called once
    """
    def __init__(self,name):
        self.name=name
        print('initialized')

if __name__ == "__main__":
    print(person('aaa'))
    print(person('bbbb'))

