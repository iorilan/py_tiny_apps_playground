import functools
import math

def cache_res(func):
    def inner(*arg, **kwarg):
        key = arg+tuple(kwarg.items())
        if key not in inner.cache:
            inner.cache[key] = func(*arg, **kwarg)
        return inner.cache[key]
    inner.cache = {}
    return inner

@cache_res
def test_compute(n):
    res= math.sqrt(n)+ math.sin(n) * math.cos(n)
    print(f'calculated result of :{n} -- {res}')
    return res


"""
    only calculated 2 times 
"""
if __name__ == "__main__":
    print(test_compute(10))
    print(test_compute(10))
    print(test_compute(5))
    print(test_compute(5))
    print(test_compute(5))
