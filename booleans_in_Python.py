""" In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:

"""

#source: https://www.w3schools.com/python/python_booleans.asp

#When you run a condition in an if statement, Python returns True or False:

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 64
b = 32 

if a == b: 
    print(f"{a} is equal to {b}")
elif a < b: 
    print (f"{a} is less than {b}")
else:
    print(f"{a} is greater than {b}")

#Evaluate two variables:
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

age = 18
candrink = age > 20 # if the age is greater than 20 then assign the value to can drink and it returns true or false. this case 
# it would return false because the age is 18 
print(candrink)

print("What is the age number")
age= input()

if age > 20: 
  print(" the age is greater than 20")
elif age <=20: 
  print("the age is less than or equal than 20")
else: 
  print("THis might hit it or not") # this is the syntax 

"""
Operator	            Description	                                                    Example	
and 	                  Returns True if both statements are true              	    x < 5 and  x < 10	
or	                      Returns True if one of the statements is true	                x < 5 or x < 4	
not	                      Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)

"""

x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)

#In fact, there are not many values that evaluates to False, except empty values, such as (), [], {}, "",
#  the number 0, and the value None.
#  And of course the value False evaluates to False.

#Functions can Return a Boolean
#You can create functions that returns a Boolean Value:

def myFunction() :
    return True

print(myFunction())

#You can execute code based on the Boolean answer of a function:
# Print "YES!" if the function returns True, otherwise print "NO!":

if myFunction():
  print("YES!")
else:
  print("NO!")

#Python also has many built-in functions that returns a boolean value, 
# like the isinstance() function, which can be used to determine if an object is of a certain data type:
# 
# Check if an object is an integer or not:

i = 200
print(isinstance(i, int))

#source https://github.com/CalebCurry/python/blob/master/beginner_python/05-logic-and-if.py
#Even lists!
my_grades = [100, 100, 100]
your_grades = [100, 100, 1]
print("Same grade?", my_grades == your_grades) #false

your_grades = [100, 100, 100]
print("Same grade?", my_grades == your_grades) #true 

#in some languages, == compares by memory address to see if same object
#this is done in python using is.
#This is known as an identity comparison
print("are grades the same object?", my_grades is your_grades) #false

#You can also do order testing for strings
#Read ABC comes before BCD?
print("A before B?", "ABC" < "BCD")

#Not operator can be used to negate an equality check
#Read A is not equal to B? 
print("A != B?", "A" != "B")