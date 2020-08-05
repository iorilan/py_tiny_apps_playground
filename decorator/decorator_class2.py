"""
    class as decorator
"""
import functools

class call_counter:
    def __init__(self, f):
        functools.update_wrapper(self, f)
        self.func = f
        self.num = 0
    def __call__(self, *args, **kwargs):
        self.num +=1
        print(f'called {self.num} times')
        return self.func(*args, **kwargs)

@call_counter
def test_call():
    print("testing")


if __name__ == "__main__":
    test_call()
    test_call()
    test_call()