
                 # we are receiving a string in the form of a time.
def timeConversion(s):
    last_two = s[-2:]# this will get the last two characters from the string./ string slicing
    if last_two == "PM" and s[:2]!="12":# if the last two == pm and the first two not equal 12
        s = str(12 + int(s[:2])) + s[2:] # convert s to 12 plus the first 2 chars, and the rest of the characters after the first two
    if last_two == "AM" and s[:2] == "12": # if the last two is AM and the first two == 12
        s = "00" + s[2:] # the string is 00 and the rest of the slice after the first two chars
    return s[:-2] # anyother option just return everything minus the last two chars. 

timeconv="07:05:45PM"
print(timeConversion(timeconv))


#source to learn it on video. https://www.youtube.com/watch?v=izgTxnsxhr4

