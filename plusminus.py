def plusMinus(arr):
    neg = 0
    pos = 0 
    zero = 0
    for i in range(len(arr)): 
        if arr[i] < 0: 
            neg += 1
        elif arr[i] > 0: 
            pos += 1
        else:
            zero+=1
  
    print(pos/len(arr))
    print(neg/len(arr))
    print(zero / len(arr))