#micro-1

def old_func():
    print("Original function is running")
def wrapper(old_func):
    def new_func():
        print("Before function call")
        old_func()
        print("After function call")
    return new_func            

now_func = wrapper(old_func)

now_func()

#micro-2

def wrapper(func):
    def new_func():
        print("Before function call")
        func()
        print("After function call")
    return new_func            
@wrapper
def old_func():
    print("Original function is running")

old_func()    

#micro-3

def wrapper(func):
    def new_func(*args, **kwargs):
        print("Before function call")
        result=func(*args, **kwargs)
        print("After function call")
        return result
    return new_func            
@wrapper
def add(a,b):
    return a+b

print(add(3,6))

#micro-4

def bad_wrapper(func):
    def new_func(*args):
        print("Before function call")
        func(*args)
        print("After function call")
    return new_func             

@bad_wrapper
def add(a,b):
    return a+b

result = add(3,6)
print(result)

#micro-5

import time 

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end-start:.6f} seconds")
        return result
    return wrapper

@timer
def compute():
    time.sleep(1)
    return "Done"

print(compute())

##micro-6-10

#....