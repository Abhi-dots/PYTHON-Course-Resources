# CONDITIONAL STATEMENTS

# WHAT ARE CONDITIONAL STATEMENTS IN PYTHON?
"""
Conditional statements are used to make decisions in a program.
They execute differenet blocks of code based on whether a condition is true or false.
"""

# IF, ELSEIF, ELSE

## IF

# mani_age = 17

# if mani_age >= 18:
#     print("Mani is Eligible for voting")
# else:
#     print("Mani is not Eligible for voting")

## ELSEIF

mani_math_marks = 84

if mani_math_marks >= 90:
    print("A+")
elif mani_math_marks >= 80:
    print("A")
elif mani_math_marks >= 70:
    print("B")
else:
    print("C") 

## NESTED IF STATEMENT

age = 25
license = False

if age >= 18:
    if license:
        print("You can drive")

## short hand if

age1 = 20

if age1 >= 18: print("Allowed")

## short hand ifelse
##### (TERNARY OPERATOR)

marks = 30

# if marks >= 35:
#     print("PASS")
# else:
#     print("FAIL")

print("PASS" if marks >= 35 else "FAIL")

priya_age = 25
priya_salary = 50000

if priya_age >= 40 or priya_salary < 60000:
    priya_salary += 5000
    print("Priya's updated salary:- ", priya_salary)
else:
    priya_salary += 500
    print("Priya's updated salary:- ", priya_salary)