number1 = int(input('Enter first integer: ')) # this is just going to take some inputs by the user
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))

minimum = number1 # assign min to the first number than compare against 

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3

print('Minimum value is', minimum)

# another way to get the minimun in python is using the minfunction 
num = min(123, 34, 5)
print(num)

# to figure out the max, python also has a max() function 
vari = max(23, 45, 100, 1)
print(vari)