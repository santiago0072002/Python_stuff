# O(n) time | 0 (1) space
#To determine how many items a list has, use the len() function:
def validsubseq(array, sequence):
    arrptr=0 
    seqptr=0
    while arrptr < len(array) and seqptr < len(sequence):
        if array[arrptr]== sequence[seqptr]:# this means that if the array at arraypointer is equal to the sequencearray at the arrayptr element
            seqptr += 1                     # add one to the sequence pointer inside the if statement
        arrptr += 1                         # regardles of what happens we are not going to go back so add one to the pointer to the main array
    return seqptr == len(sequence) # get out of the loop if the lenght of the sequence array is equal to the sequence pointer. 


list1 = [1, 2, 3, 4, 5, 6, 7, 10 ] 

list2 = [1, 3, 10]

x = validsubseq(list1,list2)
print(x)


