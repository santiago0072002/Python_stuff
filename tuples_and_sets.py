#source: https://runestone.academy/runestone/books/published/pythonds/Introduction/GettingStartedwithData.html#built-in-atomic-data-types
# a tuple is just like a list except you can't change the items in it, it is inmutable. 
# the sintax is pretty simple use () instead of square brackets. 
my_tuple=(1,2,44,"test")
print(my_tuple)# print the tuple

print(len(my_tuple))# this prints how many tuples 
print(my_tuple[2])# just like list check an element. 
# you can also slice Tuples.
#A set is an unordered collection of zero or more immutable Python data objects. 
#Sets do not allow duplicates and are written as comma-delimited values enclosed in curly braces. 
mySet = {3,6,"cat",4.5,False}
print(len(mySet))
print(False in mySet) # this is just asking is False in mySet
print("cat" in mySet) # this is just asking is False in mySet
"""
Table 6: Methods Provided by Sets in Python
Method Name

Use

Explanation

union

aset.union(otherset)

Returns a new set with all elements from both sets

intersection

aset.intersection(otherset)

Returns a new set with only those elements common to both sets

difference

aset.difference(otherset)

Returns a new set with all items from first set not in second

issubset

aset.issubset(otherset)

Asks whether all elements of one set are in the other

add

aset.add(item)

Adds item to the set

remove

aset.remove(item)

Removes item from the set

pop

aset.pop()

Removes an arbitrary element from the set

clear

aset.clear()

Removes all elements from the set
"""

yourSet = {99,3,100}
print(mySet.union(yourSet))#{False, 3, 4.5, 99, 6, 100, 'cat'}

print(mySet | yourSet)#

print(mySet.intersection(yourSet))#3

print(mySet & yourSet)#{3}

print(mySet.difference(yourSet))#{False, 4.5, 6, 'cat'}

print(mySet - yourSet)#{False, 4.5, 'cat', 6}

print({3,100}.issubset(yourSet))#True

print({3,100}<=yourSet)#True

mySet.add("house")#{False, 'house', 3, 4.5, 'cat', 6}

print(mySet)#{False, 3, 4.5, 'cat', 6, 'house'}

mySet.remove(4.5)

print(mySet)#{False, 3, 'cat', 6, 'house'}

print(mySet.pop())#False

print(mySet)#{3, 6, 'house', 'cat'}

mySet.clear()# erase everything from the set

print(mySet)#set()