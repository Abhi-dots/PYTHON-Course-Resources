# variables and datatypes

## sql
# single line comment (--) -- this is comment
# multi line comment (/* */) /* this is comment */

## python
# single line comment (#) # this is comment
# multi line comment (""") """ this is comment """

## variables
# what is variable?
# variables are used to store data for future usage (variables works as container).

## how to write variables?
name = "Gnanesh"
student_name = "chinnu"
address2 = "Gandhi road"

## how we shouldn't write variables?
# 2ndaddress = "Gandhi road"
# student-name = "ramu"

## data types
# primitive data types
# collection data types

## primitive
# integer (int), float, string, boolean

## collection
# list, tuple, set, dictionaries

## primitive data types
# INTEGER (INT)
# whole numbers= 78, 89, -67
# decimal numbers = 23.5, 12.8
sravan_marks = 92
age = 25
temperature = -10

# float
# decimal numbers = 23.5, 12.8
price = 99.99
temperature = 36.5

# string
# text data
name = "Gnanesh"
city = "Hyderabad"
comment = "It is good product"

# string concatenation
# PYTHON IS A CASE-SENSITIVE LANGUAGE
print(name + city)
full_details = name + city
print(full_details)

print(name * 3)

# Boolean
# True or False
is_loggin_success = True
is_loggin_success1 = False
print(is_loggin_success)

## collection data types
# list
# []
student_names = ["Gnanesh", "Huzaifa", "Chinnu", "Ramu", "Sravan", 8686, 7878.8987, "Gnanesh"]
#### LIST IS ORDERED
#### LIST IS CHANGEABLE
#### LIST ALLOWS DUPLICATE VALUES

# student_names = [0, 1, 2, 3, ......]
# student_names = [        -3,-2,-1]


print(student_names[2])
print(student_names[-2])

student_names[0] = "Mahesh"
print(student_names)

student_names.append("Gopal")
print(student_names)

student_names.insert(1, "Suresh")
print(student_names)

student_names.pop()
print(student_names)

student_names.remove("Mahesh")
print(student_names)

print(len(student_names))

## tuple
# ()

colours = ("red", "green", "blue")

# colours.append("yellow")
# print(colours)

# colours.remove("red")
print(len(colours))

# set
# {}
numbers = {1,2,3,4,5,6,2,3,4}
## set doesn't allow duplicate values
## set is unordered
## set is changeable

print(numbers)

numbers.add(5)
print(numbers)

numbers.remove(2)
print(numbers)

## dictionary
# {}
student = {"name" : "Gnanesh", "age" : 24, "marks" : 95, "FATHER_NAME" : "Gnanesh"}
print(student['name'])
student['marks'] = 97
print(student)

student['city'] = "Bangalore"
print(student)

student.pop("marks")
print(student)

print(student.keys())
print(student.values())

x = 10
print(type(x))
print(type(student))

x1 = "10"
x2 = int(x1)
print(type(x2))

"""
LIST - ORDERED, CHANGEABLE, ALLOWS DUPLICATES
TUPLE - ORDERED, UNCHANGEABLE, ALLOWS DUPLICATES
SET - UNORDERED, CHANGEABLE, DOESN'T ALLOW DUPLICATES
DICT - ORDERED, CHANGEABLE, KEY SHOULD BE UNIQUE
"""