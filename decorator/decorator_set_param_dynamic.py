from functools import wraps ,partial

def add_wrapper(obj, func=None):
    if func is None :
        return partial(add_wrapper, obj)
    setattr(obj, func.__name__, func)

def post_log(level, name, message, save_result):
    

    def inner_func(func):
        logname=name
        logmessage=message
        save=save_result

        @wraps(func)
        def wrapper(*arg, **kwargs):
            res = func(*arg, **kwargs)
            res_str = res if save else ''
            print(f'{logname},{logmessage} {res_str}')
            return res
        

        @add_wrapper(wrapper)
        def set_message(val):
            nonlocal logmessage
            logmessage = val
            
        @add_wrapper(wrapper)
        def set_name(val):
            nonlocal logname
            logname = val

        return wrapper
        
    return inner_func


@post_log("DEBUG", "name", "message", False)
def func1():
    return 1

@post_log("INFO", "name", "message", True)
def func2():
    return 2

if __name__ == "__main__":
    func1()
    func2()
    func1.set_name('new name')
    func2.set_message('new message')
    func1()
    func2()