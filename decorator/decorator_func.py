"""
can be used for AOP like logging/tracing or 'filtering' logic at global level
"""
import time
def exe_time(func):
    print('before declaration...')
    def inner_func(*arg, **kwargs):
        arg_str = ','.join(list(map(str,arg)))
        print(f'===args: {arg_str}===')
        
        print(f'==keywarded args ==')
        for k,v in kwargs.items():
            print(f'{k}:{v}')
        

        start = time.time()
        print('before executing...')
        res = func(*arg, **kwargs)
        end=time.time()
        total = round(end-start,2)
        print(f'after executing...total {total}')
        return res

    print('after declaration...')
    return inner_func

@exe_time
def test(n,n2,p1='a',p2='b'):
    res=0
    for i in range(n):
        wait = 0.1*i
        res+=wait
        time.sleep(wait)
    print(f'total wait :{round(res,2)} seconds')
    return wait    

test(1,2,p1='2',p2=3)