# 
import math
count = 100

# while condition if the condition is True then body. 
#condition example 5<6

while count >= 0:
	print(count)
	if count == 0:
		print("BLAAASSTT OFFF!!!")
	count-=1 


# sum_two it returns the sum of two numbers: 

def sum_two(num1, num2):
	return num1+num2


test1 = sum_two(100, 2)
print(test1)


def square_the_number(number_to_play):
	number_to_play ** 2 # this means number to play to the power of 2. 
	return pow(number_to_play, 2)# this is using the math library function pow returns the power function if i want to make it to three just change 2 ro three

print(square_the_number(8))

def iseven(numbertocheck): #this check if the number is even or not, so if the number is divisible by two and the reminder is 0 then it returns back true. 
	if numbertocheck %2 == 0: # this means if number is divisible by two
		return True
	else: 
		return False



def isOdd(number): # this is checking if the number is odd 
	return number %2 != 0 # return if number devided by 2 == and the reminder is 1. 


print(isOdd(3)) 


print(iseven(7))


def stringlen(word): # this return 
	# return len(word)
	count = 0
	for letter in word:
	
		count+=1 # increment count by one. 

	return count


print(stringlen("hello!"))
print(stringlen("banana"))

def last_letter(word):
	return word[-1]


print(last_letter("Hello!"))
print(last_letter("Banana"))


def max_number(num1, num2):
	if num1 > num2:
		return num1
	else:
		return num2

def max_number1(num1, num2, num3):
	max_number = num1

	if num1 > num2:
	    max_number = num1
	elif num2 > num3: 
	    max_number = num2
	else:
	    max_number = num3

	return max_number

def max_number2(num1, num2, num3):# convert the inputs into a list then get the max out of the list using the max(method)
	listmax = [num1, num2, num3]
	return max(listmax)




listex = [23, 24, 25]

print(max_number1(85, 35, 45))
print(max_number2(23,24,25))



def name_placement(name):
	# 1:"usain", 2:"hector", 3:"quzi"
	if name == "usain":
		return 1
	if name == "hector":
		return 2
	if name == "quzi":
		return 3

def choice_to_name(choice):
	return {"usain": 1, "me":2, "quzi":3}[choice] # this is a dictionary indexed by choice
	

print(name_placement("hector"))

def number_placement(number):
	# 1:"usain", 2:"hector", 3:"quzi"
	if number == 1:
		return "usain"
	if number  == 2:
		return "hector"
	if number == 3:
		return "quzi"

print(name_placement("hector"))

print(number_placement(3))


print(choice_to_name("usain"))# this would return the value assoociated with the key that I am passing it to. this take the key 

def choice_by_number(number):
	return {1:"usain", 2: "me", 3: "quzi"}[number] # this is a dictionary indexed by numbers, it returns the name associated with the number value, this is the syntax for it. 

print(choice_by_number(3))# this would return quzi, we have to pass the key and it would return the value

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]# turnining them in to squared

squared = []

for number in numbers: # make a loop then for each number of times the loop comes around just append the squared number to the list. 
	squared.append(number**2)

print(squared)