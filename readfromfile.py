# to read from a txt file in python it is easier if the script is in the same folder as the python script is.  
# source: https://www.youtube.com/watch?v=0EgSo7hsRWM
file = open("file1.txt", "r") # first we open the file like this: 1. Create a variable, in this case it is called file. 
f = file.readlines()   
newlist = []
for line in f:
	if line[-1] == "n":
		newlist.append(line[:-1])
	else:
		newlist.append(line)
#source for open the file and decode it with base 64: https://wireintheghost.wordpress.com/


import base64

#Open file
with open('b64.txt') as f: #Read the file into the msg variable
						   #Decode 50 times with a basic for loop
    msg = f.read()

#Decode 50 times
for _ in range(50):
    msg = base64.b64decode(msg)

print(f"The flag is: {msg.decode('utf8')}")

""" The first task was quite straight forward. 
We are required to take a file that had been base64 encoded 50 time and reverse the process revealing the original string. 
Luckily Python has a base64 library ready for us to use so the steps we need are:"""