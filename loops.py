from builtins import sum

my_friends = ["Larry", "Tarra", "skezzee", "Rushing"]

# to print everybody as a list just use the name of the list inside print. 
print(my_friends)

# to print each name individually that's when the loop comes in handy. 
for friend in my_friends: 
    print(friend) # each one here is in a different line

# to print in the same line pass the arguement end to the print method. 
for friend in my_friends: 
    print(friend, end = " ")# here we are separating each of the elements of the my_friends list by a space. 
print()# to stop the end = " " if we want to start in a new line just type the print method empty in a new line. 

#instead of iterating through a list, we can use a function called range
#This loop runs 10 times

for i in range(10 ):# another way to think about what is inside the range function is how many iterations of the loop 
    print("iteration ", i + 1, end = " ")# if we don't want to show the zero we can just add i + 1
print()


# if we want to print or use the range function to print from a certain range of numbers to another range of numbers we would do it 
# like this: 
for i in range(10, 20): 
    print("this iterations i = " , i + 1)

# if we want to count by two using the step method 
for i in range(10, 41, 2): # this means count from 10 to 41 by 2. first arguement is the number we want to start with,
    print(i, end = " ") # second number is the number we want to end and the third is the count by number. 
print()
#Go the other way. 
#9 included. -1 not included (result is 9-0)
for i in range (9, -1, -1):
    print(i, end=" ")
print()

#The third argument is called the step. we can set it to whatever
#Count down from 100 to 0, by 10s.
for i in range (100, -1, -10):
    print(i, end=" ")
print()

# the solution to the problem below count odd numbers from 0 to 100 

for i in range(1, 100, 2): 
    print(i , end = " ")
print()

# if we want to sum the numbers in the range we would use the function sum example would  be: 
for i in range(10): 
    print(i)

print(sum(range(10)))

# another way to do this would be: 
sum = 0 
for i in range(10): 
    sum+=i
    print(sum) 

# this is how you take a range and save it into a list: 
# where I learned this:: https://www.youtube.com/watch?v=s3IvdkCq2_c&t=9362s

for i in range(10): 
    print(i, end = " ")
print()

# this is how you take a range and save it into a list: we just have to use the keyword list infront of range()
# step one, create a varriable, step to use the range function with the number that you want, step 3 use the keyword list(range(10))
my_list = list(range(10))
print(my_list)



books = ["Head First Python,", " Python by Deitel,"," C# programmer # 6,", "C # for hackers,", "Linux Bibble"]
for book in books: 
    print(book, end = " ")
print()
# this is very IMPORTANT TO UNDERSTAND: here is video explanation by Caleb curry
# https://www.youtube.com/watch?v=s3IvdkCq2_c&t=9362s
# to print the element and the value we do it like this: below we have to use the len() function: 
# the question is what element each one of the books list is: 
for i in range(len(books)): # what we are doing is that we are passing to the range the len of books in other words range(len(books))
    print(i, books[i])

