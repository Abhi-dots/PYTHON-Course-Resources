# FUNCTIONS

# WHAT IS FUNCTION IN PYTHON?
"""
A FUNCTION IS A RESUABLE BLOCK OF CODE THAT PERFORMS A SPECIFIC TASK.
"""

# BASIC FUNCTION SYNTAX IN PYTHON
"""
def function_name():
    block of code
"""

def info():
    print("welcome to real data analysis, keep learning and like this video")

info()

# functions with parameters
def info(name):
    print("welcome to real data analysis " + name +" , keep learning and like this video")

name = input("Enter your name:- ")
info(name)

def student(name, course):
    print(name, "is learning", course)

student("Gnanesh", "Python")

# RETURN
def add(a, b):
    return a+b

result = add(4,7)
print(result)

# what is difference between return and print?
def add(a, b):
    print(a+b)

result = add(4,7)
print(result)

def add1(a, b):
    return a+b

result = add1(4,7)
print(result)

# default parameters
def welcome (name = "Guest"):
    print("welcome", name)

name = input("Enter your name:- ")
welcome(name)
welcome()

# keyword arguments
def info(name, age):
    print("my name is", name, "and i am", age, "years old")

info(age = 23, name = "Gnanesh")

# arbitary arguments
def numbers(*args):
    print(args)

numbers(10, 20, 30, 40)

# arbitary keyword arguments
def numbers(**kwargs):
    print(kwargs)

numbers(name="Gnanesh", age=23)

# local variables and global variables

def demo():
    x = 100
    print(x)

demo()

x = 1000
def demo1():
    print(x)

demo1()

# recursive functions

def countdown(n):
    if n == 0:
        print("Done")
    else:
        print(n)
        countdown(n-1)

countdown(3)