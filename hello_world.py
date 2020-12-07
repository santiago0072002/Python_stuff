print("Hello Python World!")
message = "Hello this is a string" 
print(message)
print(message.title()) # this is how you show words in Tittle case
print(message.upper()) # this is how you show words in All upper 
print(message.lower()) # this is how you print everything in lower cases 

val = "Parenthesis"	
print(f"{val} is {val} and we got to use the format letter f to insert it this way. Like c#")
# Python3 program introducing f-string 
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.") 

name = 'Hector'
age = 41
print(f"Hello, My name is {name} and I'm {age} years old.") # this just like c# interpolation 

# Prints today's date with help 
# of datetime library 
import datetime 
  
today = datetime.datetime.today() 
print(f"{today:%B %d, %Y}") 

print(val + name)

print(f"this so cool {val}")
x = "you tube"
print(x)


nums = [1,3,4,5,6,] # this is how you create a list with numbers in it 
nums2 = [] # this is another way to create an empty list, list is like arrays in java. 

for num in nums: # one of the things that crack me up about python is the white space/ white space would give you an error if is not indented properly. compared to other languages
	if num == 3: # it is going to take me a while to understand the indentation but in a way it does makes sense how it is set up. 
		print("found") 
		continue
	print(num)

for num in nums:
	for letter in "abc": 
		print(num, letter) # the comma is what you use to print two variables 


#to go through the loop a certain number of times we use the range function so if we want to go through the loop 10 times below we will write 

for i in range(10): 
	print(i + 1)


# while loop will keep going until a condition is meat 
x = 0

while x < 10: 
	if x == 5: 
		continue
	print(x)
	x += 1


x = 0

while True: 
	print(x) # this would be an infinite loop, ctr c to stop it. 
	x += 1