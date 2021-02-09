#N(Log(n)) + mLog(m))time | O(1) space

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0 
    smallest = float("inf")
    current = float("inf")
    smallestpair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]	
    return smallestPair


list1 = [1, 2,3, 4,5,10,25]
list2 = [26, 30, 40]
print(smallestDifference(list1, list2))