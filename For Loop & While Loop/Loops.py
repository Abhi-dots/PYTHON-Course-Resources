# LOOPS

# WHAT IS A LOOP IN PYTHON?

"""
A LOOP IS USED TO EXECUTE A BLOCK OF CODE REPEATEDLY UNTIL A CONDITION BECOMES FALSE
OR UNTIL ALL ITEMS IN A SEQUENCE ARE PROCESSED
"""

# TYPES OF LOOPS IN PYTHON

"""
1. FOR LOOPS
2. WHILE LOOPS
3. NESTED LOOPS
4. LOOP CONTROL STATEMENTS
   * BREAK
   * CONTINUE
   * PASS
"""

# FOR LOOP
# for loops are used when the number of iterations is known.

# range(start, end, step)
for i in range(5):
    print(i, end = " ")

for i in range(1, 4):
    print(i)

for i in range(1, 11, 2):
    print(i)
# 1 2 3 4 5 6 7 8 9 10 11

name = "Gnanesh"
for m in name:
    print(m)

fruits = ["Apple", "Mango", "Banana"]
for fruit in fruits:
    print(fruit)

fruits = ("Apple", "Mango", "Banana")
for fruit in fruits:
    print(fruit)

student = {"name" : "Gnanesh", "age" : 24}

for key, value in student.items():
    print(key, value)

while loop:
    i = 1

while i < 5:
    print(i)
    i = i + 1     #i += 1

password = ""

while password != "admin":
    password = input ("Enter password:- ")

print("Login Successful")

while True:
    print("Hello")

# nested loops
for i in range(1, 4): #i = 3
    for j in range(1, 4): #j = 1
        print(i, j)

# break
# stops the loop immediately

for i in range(1, 11):
    if i == 6:
        break
    print(i)
# # 1 2 3 4 5 6 7 8 9 10

for i in range(1, 11):
    if i == 6:
        continue
    print(i)
# 1 2 3 4 5 6 7 8 9 10

for i in range(5):
    pass
print("Program completed")