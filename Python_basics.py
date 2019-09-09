#!/usr/bin/env python
# coding: utf-8

# CLASS 1 - Data structures
#
# Variables
# A name that is used to denote something or a value is called a variable. In python, variables can be declared and values can be assigned to it as follows

#Integer
some_number = 2 #Integer: Integer is just any whole number
#Float
some_decimal_number = 5.2 #Floating Point or Float: a variable with a fractional value. Numbers created using a float variable declaration will have digits on both sides of a decimal point.
some_number2 = 2.0 #Even this is considered as a float since the decimal is specified

#Strings
some_text = 'Hello' #String: A string is usually a bit of text you want to display
some_number_string = '0' #A number inside quotes is still considered a string
double_quote = "Hello" #Strings can be enclosed by either single or double quotes

#Lists (Values are enclosed by []
my_list = [1,2,3,4,'hello','Python', 7.9,8] #List can have any number of values and mixed data types. Lists are mutable and values can be added and removed

#Tuples (Values are enclosed by ()
my_tuple = (1,2,3,4,'Hello','python',7.9,8) #Tuples are similar to lists but they are immutable. i.e you cannot add or remove values from a tuple

#Dictionaries (Have keys and values. Keys and values can be of any data type but keys cannot be repeated
my_dict = {'some key': 'some value', 'key2': 'value2', 'key3': 'value3', 4 : 'Value for 4', 'key for 5': 5}

# Print statement

#Print statement
print('Hello world') #Prints hello world
print('Print value of some_number  ==>', some_number) #Prints the variables

# Question:
#     Create a variable of name flower_name and assign rose as its value
#     Create a variable of name my_number and assign 5 as its value

#Enter your answers here


# Checking data types

print(type(123))

print(type(12.23))

print(type('hello'))

print(type([1,2,3,4,'five']))

print(type({'a': 1, 'b': 'second', 'c': [1,2,3]}))

print(type((1,2,3,4,5,6)))


# Question:
#     print your name using print statement.

#Enter your answer here

# Operators
# Python Arithmetic Operators:
# Assume variable a holds 10 and variable b holds 20, then −
# a + b = 30
# a – b = -10
# a * b = 200
# b / a = 2
# b % a = 0
# a ** b =10 to the power 20
# 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0

# Python Comparison Operators:
# Assume variable a holds 10 and variable b holds 20, then −
# (a == b) is not true.
# (a != b) is true.
# (a <> b) is true. This is similar to != operator.
# (a > b) is not true.
# (a < b) is true.
# (a >= b) is not true.
# (a <= b) is true.

# Python Assignment Operators
# Assume variable a holds 10 and variable b holds 20, then −
# c = a + b assigns value of a + b into c
# c += a is equivalent to c = c + a
# c -= a is equivalent to c = c - a
# c *= a is equivalent to c = c * a
# c /= a is equivalent to c = c / a
# c %= a is equivalent to c = c % a
# c ** = a is equivalent to c = c ** a
# c //= a is equivalent to c = c // a
#
# Python Logical Operators
# x in y, here in results in a 1 if x is a member of sequence y.
# x not in y, here not in results in a 1 if x is not a member of sequence y.
#
# For more information, please refer: https://www.tutorialspoint.com/python/python_basic_operators.htm

#Operators
print('10 + 10 = ', 10+10)
print('100 - 10 = ', 100-10)
print('10 * 10 = ', 10*10)
print('10 / 5 = ', 10/5)
print('10**2 = ', 10**2) #Prints 10^2 (10 to the power 2)
print('8 % 4 = ', 8 % 4) # % operator prints the remainder
print('5 // 2 = ', 5//2) # Similar to divide but prints the obtained to the nearest integer

#Assertion
z = 1
print('z == 1 =>', z==1) # This returns true because z = 1
print('z > 1 =>' , z>1) # Prints false because z is not greater than 1

# Some common inbuilt functions:

#Some common inbuilt functions
print('round(5.222) = ',round(5.222)) #Rounds the value and prints
print('abs(-2) = ',abs(-2)) #Prints absolute value
print('int(5.555) = ',int(5.555)) # Converts value to an integer and prints
print('len("hello)" = ', len('hello')) # Prints number of characters in the string
print('max([1,2,3,4,5]) = ', max([1,2,3,4,5])) #Prints largest value of a list or tuple
print('min([1,2,3,4,5]) = ', min([1,2,3,4,5])) #Prints smallest value of list or tuple

# Question:
#     print the rounded value of 121.9928381
#

#Enter your answer here

# String manipulation functions:
# Strings are a special type of a python class. As objects, in a class, you can call methods on string objects using the .methodName() notation.
# The string class is available by default in python, so you do not need an import statement to use the object interface to strings.

# go over ? mark after if you are not sure what method does.
firstVariable = 'Hello World'
print(firstVariable.lower())
print(firstVariable.upper())
print(firstVariable.title())

# To look up what each method does
help(firstVariable.lower)

a=firstVariable.split(' ')
print(a) #Splits string into a list

print(' '.join(a))

print("0" + "1")

print("0" * 3)

print("Fizz" + "Buzz")

# Question:
#     1. Assign the string "1|2|3|4|5" to a variable
#     2. Convert the string to ['1', '2', '3', '4', '5']

#Enter your answer here

# Getting user input:

user_variable = raw_input('Enter your input here: ') #Asks for input when you execute the program
print('The value you entered is ', user_variable)

# Question:
#    Get a value from user and assign it to a variable

#Enter your answer here


# Accessing list values and list slicing:
# index stars at zero

my_list = [1,2,3,4,5,6,'seven','eight',9]
print('Lists elements can be accessed using index')
print(my_list[0]) #Prints first element of list
print(my_list[2]) #Prints third element of lists
print(my_list[1:4]) #Prints second, third and fourth elements of list (list slicing)
my_list.append('adding new value') #Adds a new value as last element of list
print(my_list)
my_list.insert(5, 'Hello class') # Inserts value at 5th position
print(my_list)
my_list.pop(2) #Removes third element in the list
print(my_list)
my_list.remove('Hello class') #Removes a specific element of the list
print(my_list)

my_list.reverse()
print(my_list)

# Question:
#    Get a value from user and assign it to a variable and print the variable

#Enter your answer here


# Accessing values in dictionaries:

my_dict = {'some key': 'some value', 'key2': 'value2', 'key3': 'value3', 4 : 'Value for 4', 'key for 5': 5}
print('Dictionary values can be accessed using index')
print(my_dict['some key']) #Prints value for key "some key"
print(my_dict[4]) #Prints value for key 4
print(my_dict.keys()) #Print all keys of dictionary
print(my_dict.values()) #Print all values of a dictionary

# Logical operators revision
#
# Logical Operator
# Description
#
#
#     and : If both the operands are True then condition becomes True
#     or : If any of the two operands are True then condition becomes True
#     not : Used to reverse the logical (not False becomes True, not True becomes False

# if else statements:

# if Statements

# Notice you have to indent after you start a if statement.
num = 3
if num == 3:
    print(num)

# Nothing is outputted because num > 10 is FALSE
num = 3
if num > 10:
    print(num)

num = 3
if num % 3 == 0:
    print("Fizz")

num = 10
if num % 5 == 0:
    print("Buzz")

if True:
    print("This was True")

if False:
    print("Nothing printed")

# else statements
# Must be after an if or elif statement. There can be at most one else statement. Will only be executed if all the "if" and "elif" statements above it are False.

"""We will execute what is inside the else statement
because num is not greater than 3
"""
num = 1
if num > 3:
    print("Hi")
else:
    print("number is not greater than 3")

"""We will execute what is inside the if statement because num > 4"""
num = 4
if num > 3:
    print("Hi")
else:
    print("number is not greater than 3")


num = 3
if num % 2 == 0:
    print("Your integer is even")
else:
    print("Your integer is odd")

# if-elif-else combined
#

num = 21
if num > 50:
    print('num is larger than 50')
elif num == 21:
    print('num = 21')
else:
    print('Catchall condition')

my_num = 5
if my_num % 2 == 0:
    print("Your number is even")
elif my_num % 2 != 0:
    print("Your number is odd")
else:
    print("Are you sure your number is an integer?")

# You can have mulitple elif statements.
# Remember only the first True statement has its block of code executed.

dice_value = 1
if dice_value == 1:
    print('You rolled a {}. Great job!'.format(dice_value))
elif dice_value == 2:
    print('You rolled a {}. Great job!'.format(dice_value))
elif dice_value == 3:
    print('You rolled a {}. Great job!'.format(dice_value))
elif dice_value == 4:
    print('You rolled a {}. Great job!'.format(dice_value))
elif dice_value == 5:
    print('You rolled a {}. Great job!'.format(dice_value))
elif dice_value == 6:
    print('You rolled a {}. Great job!'.format(dice_value))
else:
    print('None of the conditions above (if elif) were evaluated as True')