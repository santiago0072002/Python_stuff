
                 # we are receiving a string in the form of a time.
def timeConversion(s):
    last_two = s[-2:]# this will get the last two characters from the string./ string slicing
    if last_two == "PM" and s[:2]!="12":# if the last two == pm and the first two not equal 12
        s = str(12 + int(s[:2])) + s[2:]
    if last_two == "AM" and s[:2] == "12": 
        s = "00" + s[2:]
    return s[:-2]

timeconv="07:05:45PM"
print(timeConversion(timeconv))


#source to learn it on video. https://www.youtube.com/watch?v=izgTxnsxhr4

