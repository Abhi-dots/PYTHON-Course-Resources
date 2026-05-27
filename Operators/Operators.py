# OPERATORS

# WHAT IS OPERATOR IN PYTHON?
# OPERATORS ARE SYMBOLS USED TO PERFORM OPERATIONS ON VARIABLES AND VALUES.

"""
1. ARITHMETIC OPERATORS
2. ASSIGNMENT OPERATORS
3. COMPARISION OPERATORS
4. LOGICAL OPERATORS
5. IDENTITY OPERATORS
6. MEMBERSHIP OPERATORS
7. BIWISE OPERATORS
"""

# ARITHMETIC OPERATORS
# +, -, *, /, //, %, **

a = 10
b = 3

print(a+b)   # output -> 13
print(a-b)   # output -> 7
print(a*b)   # output -> 30
print(a/b)   # output -> 3.33
print(a//b)  # output -> 3
print(a%b)   # output -> 1
print(a**b)  # output -> 10^3 -> 1000

"""
3)10(3.3
   9
  ---
   10
    9
   ---
    1
"""

# ASSIGNMENT OPERATORS
# =, +=, -=, *=, /=

x = 10
print(x)

x += 5  # x = x + 5
print(x)


# comparison operators
# ==, !=, >, <, >=, <=
n = 10
m = 10

print (n == m)
print (n != m)
print (n >= m)

n1 = 10
m1 = 5

print (n1 > m1)
print (n1 < m1)


# LOGICAL OPERATORS
# AND, OR, NOT

# and
a1 = 10
print(a1 > 5 and a1 < 20) # both conditions true

print(a1 > 5 or a1 < 9) # Any one condition come true

print(not(a1 > 5))

# identity operators
# is, is not

a2 = [1, 2] # 1001 memory
b2 = a2  # 1001 memory

print(a2 is b2)

a2 = [1, 2] # 1001 memory
b2 = [1, 2]  # 1002 memory

print(a2 is b2)


# membership operators
# in, not in

list1 = [1, 2, 3, 4]
print(2 in list1)
print(10 in list1)
print(10 not in list1)

# bitwise operators
# &, |, ~, <<, >>

# &
a3 = 5
b3 = 3

print(a3 & b3)  # output -> 1

#            2^3  2^2  2^1 2^0
#             8    4     2   1
# a3 = 5 ->    0    1    0    1   -> 0101
# b3 = 3 ->   0     0    1    1   -> 0011
                               #     ----
                               #     0001

# ~
nm1 = 5
print(~nm1)

# <<
ab = 5  # 0101  -> 0 1010 -> 8+2 -> 10
print(ab << 1)