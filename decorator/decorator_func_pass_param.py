from functools import wraps 

def post_log(level, name, message, save_result):
    def inner_func(func):
        @wraps(func)
        def wrapper(*arg, **kwargs):
            res = func(*arg, **kwargs)
            res_str = res if save_result else ''
            print(f'{name},{message} {res_str}')
            return res
        return wrapper
    return inner_func


@post_log("DEBUG", "name", "message", False)
def func1():
    return 1

@post_log("INFO", "name", "message", True)
def func2():
    return 2

if __name__ == "__main__":
    print(func1())
    print(func2())