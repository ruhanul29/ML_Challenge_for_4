#micro-1

try:
    age = int(input("Enter your age"))
    print("Your age is: ",age)
except ValueError:
    print("Numbers only")    
    
#micro-2

x = 0

try:
    print(100/0)
except ZeroDivisionError:
    print("Can not divide by 0")        

#micro-3

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: ")) 
    print(a/b)
except (ValueError, ZeroDivisionError):
    print("Invalid input or divided by 0")
finally:
    print("Execution complete")  

#micro-4

try:
    num=int(input("Enter a number: "))
    if num<0:
        raise ValueError('No negatives')
    print("You entered: ",num) 
except ValueError as e:
    print(e)
                        