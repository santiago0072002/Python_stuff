# source https://www.youtube.com/watch?v=SoFjox6VJGs&list=PLtbC5OfOR8aops-jzO_fzNJ-6Q6_Tblro&index=3

def anagramSolution1(s1,s2):
    stillOK = True # this flag means we are still looking for an anagram
    if len(s1) != len(s2): # this check to see if the size of both of the strings are equal if not then no need to go through the code, set still ok to false
        stillOK = False

    alist = list(s2) #Convert String to a list
    pos1 = 0 # variable to keep track of where you are at in the first list. 

    while pos1 < len(s1) and stillOK:#outer loop 
        pos2 = 0 # variable to keep track of where you are at in a second list. 
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

print(anagramSolution1('aabcd','dcba'))


def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)
    if len(s1) != len(s2): return False # if the size of both of the lists are not the same just return false

    alist1.sort() # sort both of the lists
    alist2.sort()

    pos = 0 # use this pointer to keep track of where you are at in the list. 
    matches = True # set bool matches to True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde','edcba'))




def my_anagramSolution(list1, list2):
    list1 = list(list1.lower())# convert strings to a list just in case the input the input is a tuple or something along those lines. 
    list2 = list(list2.lower())
    ok = True
    if (len(list1)) !=  (len(list2)):
        return False

    list1.sort()
    list2.sort()

    listptr = 0
    
    while listptr < len(list1) and ok:
        if list1[listptr] in list2[listptr]:
            listptr += 1
        else:
            ok = False
    return ok

print("My Solution result is", my_anagramSolution("Readme", "MeRead"))