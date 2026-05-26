# INPUT AND OUTPUT

# WHAT IS INPUT?
# INPUT MEANS TAKING DATA FROM THE USER DURING PROGRAM EXECUTION.

# WHAT IS OUTPUT?
# OUTPUT MEANS GIVING INFORMATION TO THE USER DURING PROGRAM EXECUTION.

# INSTAGRAM
# ENTER YOUR USERNAME:- USERNAME1234
# ENTER YOUR PASSWORD:- PASSWORD9900

# OUTPUT
# LOGGIN SUCCESSFUL 

NAME = input("Enter your name:- ")
print("You entered name is:", NAME)

NAME = input("Enter your name:- ")
AGE = int(input("Enter your age:- "))

print(NAME)
print(AGE)

print(type(NAME))
print(type(AGE))

a, b = input("Enter any two values:- ").split()

print(a)
print(b)

# map
a, b = map(int, input("Enter two values:- ").split())
print(type(a))
print(type(b))

name = input("Enter your name:- ")
age = input("Enter your age:- ")

print("Your name is ", name, "and age is ", age)

# formatted output - f-string
print(f"Your name is {name} and age is {age}")