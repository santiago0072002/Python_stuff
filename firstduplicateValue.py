#O (n) time | O (n) space

def firstDuplicateVal(arrayList):
    seen = set()
    for idx in arrayList: 
        if idx in seen:
            return idx
        seen.add(idx)
    return -1 


listex = [1 , 2, 3,4,5 ,6,1,2]

print(firstDuplicateVal(listex))