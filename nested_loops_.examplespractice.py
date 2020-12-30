"""Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop": """
#Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

""" The result of the aboved loop would be. 
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
""" 

outerloopnums= [1,2,3]
innerloopletters=["a","b","c"]

for i in outerloopnums:
    for j in innerloopletters:
        print(i,j)



"""
1 a
1 b
1 c
2 a
2 b
2 c
3 a
3 b
3 c
""" 

# another way to do nested for loops is as follows: Example 
numbers = [1, 2, 3]
days = ["Sunday", "Monday", "Tuesday"]
for i in numbers:
    print(i)
    for j in days:
        print(days)

numbers = [1, 2, 3]
days = ["Sunday", "Monday", "Tuesday"]
for i in numbers:
    for j in days:
        print(i, days)