from time import time

def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(1000000):
        i*5
@performance
def long_time2():
    print('2')
    for i in list(range(1000000)):
        i*5

long_time() # took 0.10994887351989746 s
long_time2() # took 0.1427900791168213 s