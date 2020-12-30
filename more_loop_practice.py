""" 
source: https://www.w3schools.com/python/python_lists_loop.asp
Python For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
The for loop does not require an indexing variable to set beforehand.
To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
To determine if a specified item is present in a list use the in keyword:
"""

#Print each fruit in a fruit list:
# Print all items in the list, one by one:
fruits = ["apple", "banana", "grapes"]
for fruit in fruits:
    print(fruit)

#print the first 10 natural numbers
for num in range(11):
	print(num)

#Looping Through a String
#Even strings are iterable objects, they contain a sequence of characters:

for x in "bananas":
    print(x)

number = 0 

while number <= 10:
	print(number)
	number+=1

lastNumber = 6 
for row in range(1 + lastNumber):
	for column in range(1 , 1 + row):
		print(column, end = " ")
	print("")	

""" 
the solution on top print this pattern. 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
""" 

# Accept number from user and calculate the sum of all number between 1 and given number
"""
Syntax
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
range(start, stop, step)
Parameter Values
Parameter	Description
start	Optional. An integer number specifying at which position to start. Default is 0
stop	Required. An integer number specifying at which position to stop (not included).
step	Optional. An integer number specifying the incrementation. Default is 1

 """
for x in range(6):
    print(x)
#Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: 
# range(2, 6), which means values from 2 to 6 (but not including 6):

for x in range(2, 6):
    print(x)
print("Example Break line-------------------")
sum1 = 0
n = int(input("Please enter number "))
for i in range(1, n+1, 1):
    sum1 += i
print("\n")
print("Sum is: ", sum1)

#Create a sequence of numbers from 0 to 5, and print each item in the sequence:

x = range(6)
for n in x:
    print(n)

# Print i as long as i is less than 6:


i = 1
while i < 6:
  print(i)
  i += 1

# With the break statement we can stop the loop even if the while condition is true:
# With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

i = 1
while i < 5:
	if i == 3:
		break
	print(i)
	i+=1



i = 0
while i < 6: 
    i+=1
    if i == 3:
        continue
    print(i)
   

# With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

""" Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable. 

The iterable created in the example below is [0, 1, 2].

You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.

Remember to increase the index by 1 after each iteration.
""" 
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])