ages = [12, 24, 34]# this is how you make a list in python
people = ["me", "you", "them"]

# list methods resources: https://www.programiz.com/python-programming/methods/list/index

for age in ages: 
    print(age)

print(people)
people.sort(reverse=True)#sort is how you sort the list, understand the sorted method because it is different from the sort() method. 
# the reverse method can be added if we want to reverse stuff using the sort method. 
print(people)
# If you want a function to return the sorted list rather than change the original list, use sorted().
#example 
# resources = https://www.programiz.com/python-programming/methods/list/sort

print(sorted(people, reverse = True))
print("testing")
print(len(people)-1)

print(ages)# this is how you display stuff in the list in python. 

print(people)

my_favorite_things = ["working out", 9, ["programming", "watch TV"]]
print(my_favorite_things)
my_favorite_things[0]= "playing outside"# this is how you change stuff in the list in python 
print(my_favorite_things)

print(len(my_favorite_things))
# this is how you make a copy of the list with the : symbol example below 

copy = my_favorite_things[:]
copy1 = my_favorite_things.copy() # or we can use the copy method and assign it to another variable. 
print(copy1)

# Python3 code to iterate over a list
# https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
list = [1, 3, 5, 7, 9]


  
# getting length of list
length = len(list)
  
# Iterating the index
# same as 'for i in range(len(list))'
for i in range(length):
    print(list[i])
"""
Return Value from List index()
The index() method returns the index of the given element in the list.
If the element is not found, a ValueError exception is raised.
Note: The index() method only returns the first occurrence of the matching element.

""" 

vowels = [ "a", "e", "i", "o", "u"]

index = vowels.index("e")
print("the index of e is", index)
# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index("i")
print("the index of 'i' is at index", index)

# if an index is not present on the list we get an error. 
# index of'p' is vowels
# index = vowels.index('p')
# print('The index of p:', index)

# The extend() method modifies the original list. It doesn't return any value.

# language list
language = ['French', 'English']

# another list of language
language1 = ['Spanish', 'Portuguese']

# appending language1 elements to language
language.extend(language1)

print('Language List:', language)
# the output will be Language List: ['French', 'English', 'Spanish', 'Portuguese']

    # Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
  
# Using for loop
for i in list:
    print(i)

# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
  
# Getting length of list
length = len(list)
i = 0
  
# Iterating using while loop
while i < length:
    print(list[i])
    i += 1

# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
  
# Using list comprehension
[print(i) for i in list]

# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
  
# Using enumerate() 
for i, val in enumerate(list):
    print (i, ",",val)

# Python program for
# iterating over array
#import numpy as geek
  
# creating an array using  
# arrange method
#a = geek.arange(9)
  
# shape array with 3 rows  
# and 4 columns
#a = a.reshape(3, 3)
  
# iterating an array
#for x in geek.nditer(a):
 #   print(x)
#https://www.w3schools.com/python/python_lists.asp
# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.
# To determine how many items a list has, use the len() function:
exampleList = [1,2, 3,4,5,6,7,8]
print(len(exampleList))# if we write len parenthesis and name of the list if going to give me how many items are in the list.

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
#thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
#print(thislist)

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered and changeable. No duplicate members.
""" 
# https://www.w3schools.com/python/python_lists_access.asp

# print the second item in the list
print(exampleList[1])

#To determine if a specified item is present in a list use the in keyword:
#Check if "apple" is present in the list:this would be equal to contains() in Java. 

thislist = ["apple", "banana", "cherry"]
if "grape" in thislist:
    print("Yes, 'apple' is in the fruits list")
elif "grape" is not thislist: 
    print("not in this list")
    thislist.append("grape")
    print(thislist)
# lets copy thislist and assign it to something else
thislistcopy = thislist.copy()
print(f"this is a copy of thislist and it contains {thislistcopy}")
print("we can compare the two list as follows", thislist, thislistcopy)
print("""when changing data we have to be careful becuase the same address
 location of the original is the same address location of the copy""")
print("the address location of the first list element[1] is:  ", id(thislist[1]))
print("the address location of the copied list element[1]is:  ",id(thislistcopy[1]))

# to copy the list without affecting the location we might want to use the deep copy method 
# we have to import it first and use it in the example below. 
import copy

deepcopythislist = copy.deepcopy(thislist)

print(id(deepcopythislist))
print(id(thislist))
# lets add something else to thislist, remember append put it at the end. insert is by index. 
thislist.append("mangos")
print(thislist)
thislist.insert(0, "avocato")# the insert method if you give it an index is going to push everything to the right
# in this example I pushed everything to the right by inserting avocato to index 0. 
print(thislist)

# deleting stuff from the list use the del key word. example. 
del thislist[1] # that would delete the second element of the list, remember list starts at 0
  
