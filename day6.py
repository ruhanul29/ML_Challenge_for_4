#micro-1

x = 10

def change_x():
    x - 20
change_x()
print(x)    

#micro-2

def add (a,b):
    print(a+b)

res = add(5,5)
print(res)    

#micro-3

def connect(port=3306):
    print(f'conecting to {port}')

connect()
connect(5432)

#micro-4

def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(9))