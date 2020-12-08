msg = "Hello \n world"# \n is the next line of the escape characters same as using printf in java and c# 
print(msg)
# single quotes and double quoates are the samething 

mssg = "Youre' preety"
print(mssg)
msg2 = 'You say "eewww"'
print(msg2)

print(mssg + msg2)
print(mssg, msg2)
full_message = mssg + "..." + msg2
print(full_message)
msg = ("this is a really, really" 
" really really long string") # this is another way to write strings in two lines. 
print(msg)

poem = """ this is so crazy that I can type this in this line 
then do this and it will show in the other line, 
but this is not the only way to show it in python. I thought this was commenting in python 
when using three double quotes but I guess it is not the only way to use them. """
print(poem)

# next we are going to get each character of a string. 
name = "Hector Santiago"
print(name[1]) # this would grab the e of the value Hector so basically index of in python is the name of the variable and follow by a square brackets

print(name[-1])# this is how you grab the last letter of the name Hector Santiago 

# slicing 
print(name[5:])# this means grab everything after index number 5 this would print r Santiago
print(name[:5])# this means grab everything upto wall character number 5 in the string this would grab Hecto
print(name[0:6])# grab from 0 to 6 but don't include 6. 
msg = "please subscribe"

print(len(msg)) # this is how we get the count of a string 
# the len function is very useful to know. this will be used to some of the loops. 
# how to tell the user your  message is 16 characters long
print(" your message is", len(msg), "characters long")
print(" your message is "+ str(len(msg))+ " characters long")

me = "Caleb"

#escape character example
print("\n")

me = "C\ta\tl\te\tb\n"

print(me)

#can also use single quotes
you = 'Subscriber'

me = "Caleb" #reset to normal

#passing multiple arguments to print
print(me, you)

#double quotes and single quotes work the same way with the exception of working with quotes inside.
#here are some examples:

single_quotes = 'She said "Hi"'
print(single_quotes)

double_quotes = "She said \"Hi\""
print(double_quotes)

single_quotes = 'I\'m learning!'
print(single_quotes)

double_quotes = "I'm learning!"
print(double_quotes)

#notice we have to escape the same quote as the surrounding quote

#Here are the other escape sequences:
#https://docs.python.org/2.0/ref/strings.html

#Notice that if you want to print \ you must put two
print("\\")

#you can also prefix with r which will make a raw string (ignoring escapes except same quote)
print(r'as raw as I\'ve ever seen. \/\/ () \/\/. \t' ) #only \' is escaped



########## CONCATENTATION ##########

#Use a + to concatenate
msg = me + " + " + you
print(msg)

#Can use comma separated values in print. Automatically uses spaces between
print(me, "+", you)

#You can automatically concatenate literals (actual values with quotes as opposed to variables)
#by putting them one after the other. This is ideal if you need to split a large string up 
#onto multiple lines.
print("my " "name "
    "is " "Caleb")

#You can also use multiline string
print("""Name: Caleb
Age: 58""")

#skip newline using \ (without it, it would go down a line each line)
print("""\
Name: Caleb. \
Age: 58""")

"""You may see
them as multi-
line comments even
if they technically
are not. 
https://stackoverflow.com/questions/7696924/is-there-a-way-to-create-multiline-comments-in-python
"""

########## INDEXES ##########

#It's very common to grab particular characters within a string
#this is also common for collections when we get to em.
msg = "This is a very important message."
print(msg[5]) 

#indexing is zero based. This means 0 will get the very first character:
print(msg[0])

#This value is returned and can be assigned to a variable or used in an expression
first_letter = msg[0]
print(first_letter + "acos")

#You can also index from the right.
period = msg[32] #from left
print(period)
period = msg[-1] #from right
print(period)
#This may be obvious, but we do not use -0 to get the first element from the right as we would
#use 0 to get the first element from the left. (Side note) -0 actually is 0:
print(-0) #(side note)
print(0 == -0) #0 == 0 (side note)

########## SLICING #########

#repeating this for ease of reading:
msg = "This is a very important message."

#We can pass two numbers in for the index to get a series of characters.
#left is included. Right is excluded.

#this will get 2 characters (from index 1 - 3 with 3 not included...we are left with index 1 and 2. 
print(msg[1:3]) #hi

#You can also leave off first to start at beginning
#or leave off second to go to end
print(msg[:5]) #print index 0-4 (because 5 is excluded, remember)
print (msg[1:]) #from index 1 to end

#We can also use negatives. Here is how you get the last 8 characters:
print(msg[-8:]) #start 8 from right and go to end

#out of range index
#Grabbing an out of range index directly will cause an error. 
#But incorrect ranges fail gracefully.
#print(msg[42]) #doesn't work
print(msg[42:43]) #works 


########## IMMUTABILITY ##########

#Strings are immutable, meaning they can't change.
cant_change = "Java is my favorite!"

#cant_change[0] = K .....nope. Sorry Kava (my dog)

#generate new string from old:
#Kava is my favorite!
new = 'K' + cant_change[1:]
print(new)

#Python is my favorite!
fav_language = "Python " + cant_change[5:]
print(fav_language)

#Java is actually coffee
coffee = cant_change[:8] + "actually coffee" #grab first 7 characters (index 8 not included)
print(coffee)

#operations that appear to change string actually replace:
#Java is actually coffee (contrary to popular belief).
coffee += " (contrary to popular belief)."
print(coffee)

########## GETTING STRING LENGTH ##########

#There is a function we can use....
#similar to how we invoke print to do something for us (output to console)
#we can invoke len to count for us:

print(len(coffee))

#for those from other languages...
#notice we do not say coffee.len()
#coffee.len() XXXXXX
#nope.

#last index is always len() - 1.
name = "Caleb"
print("index 4:", name[4]) #b
print("len(name)", len(name)) #length is 5


########## MORE STRING WORK ##########

#How to convert a number to a string
length = len(name)

print("Length is " + str(length))

#this works however sometimes you just need one combined string instead of components.
#when we use a comma, we are passing in data as separate arguments. 
#fortunately, print knows how to handle it. Other times, we must pass in one string.
#WARNING --> Commas automatically print a space.
print("length is ", length)

#an example of this is if we need a variable. We cannot use a comma:

#BAD
msg = "length is", len(name)
print(msg) #NOT WHAT WE WANTED!

#GOOD
length = len(name)
msg = "length is " + str(length)
print(msg)

#EVEN BETTER
#We can also nest function calls:
print("length is " + str(len(name)))
#The order in which these are invoked are in to out...
#len(name) is first which returns a number.
#this number is passed to str which converts it to a string
#this string is then concatenated with the string on the left
#this final string is then passed to print

#That's the end of your introduction to strings!

#Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

#However, Python does not have a character data type, a single character is simply a string with a length of 1.

#Square brackets can be used to access elements of the string.
# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])
# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

 # To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))

# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt)# this would print True 


#check if free is present in txt
if "free" in txt: 
    print("Yes 'free' is in Txt")

#Check if "expensive" is NOT present in the following text:
if "expensive" not in txt: 
    print("it is not there")

#    Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])# this would display llo

#Get the characters from position 2, and all the way to the end:

print(b[2:])

# Use negative indexes to start the slice from the end of the string:

print(b[:-1])
#Get the characters:

#From: "o" in "World!" (position -5)

#To, but not included: "d" in "World!" (position -2):

print(b[-5:-2])

#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())


# The lower() method returns the string in lower case:
print(a.lower())

print(a.title())

# removing white space I need to use the strip method.  
# the strip()method removes any whitespace from the beginning or the end:
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J")) # this means replace J for H in Hello world it would show as Jello World, the comma
# basically means for, Replace the H for the letter J. 

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))# returns ['Hello', ' World!']

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World concatenated"
c = a + b
print(c)
# to add a space just add " "
c = a + " "+ b
print(c)

# we can combine strings and numbers by using the format() method!

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# this is another way to show a string and a number in the same line. 
age = 36
txt = "My name is John Test1 , and I am"
print(txt,age)#My name is John Test1 , and I am 36

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))# I like this way becuase it has more use than everything else. 
print("my Name is Hector and my age is {age}")# this is another way to show the age 
print(f"my Name is Hector and my age is {age}")# this is another way to show the age 

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."#I want to pay 49.95 dollars for 3 pieces of item 567.
print(myorder.format(quantity, itemno, price))

"""
Escape Characters
Other escape characters used in Python:

Code	Result	Try it
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

