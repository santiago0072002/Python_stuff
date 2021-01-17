def diagonal_dif(array, number): 
# pointers to diagonals
    d1 = 0 
    d2 = 0

    for i in range(0, number):
        for j in range(0, number):
            # finding sum of primary diagonal 
        
            if i == j: 
                d1 += array[i][j]

            # finding sum of second diagonal 
            if i == number -j -1:
                d2 += array[i][j]

    # Absolute difference of the sums 
    # across the diagonals             
    return abs(d1 - d2)
number = 3
array1 = [[11, 2, 4], 
       [4 , 5, 6], 
       [10, 8, -12]] 

def difference(arr, n): 
  
    # Initialize sums of diagonals 
    d1 = 0
    d2 = 0
  
    for i in range(0, n): 
        print(d1)
        d1 = d1 + arr[i][i]
        print(arr[i][i]) 
        print(d1)
        d2 = d2 + arr[i][n - i - 1]
        print(d2)
        print(arr[i][n - i - 1])
        print(d2)
          
    # Absolute difference of the sums 
    # across the diagonals 
    return abs(d1 - d2) 

# source https://www.youtube.com/watch?v=ef0ts1cVWYc
def diagonalsol(array):
    left_to_right = 0
    right_to_left = 0
    rows = len(array)
    columns = len(array[0])

    i = 0
    j =0 
    k = 0; 
    l = len(array) - 1

    while i < rows and j < columns and k < rows and l >= 0: 
        left_to_right += array[i][j]
        right_to_left += array[k][l]
        i += 1
        j += 1
        k += 1
        l -= 1

    return abs(left_to_right - right_to_left)


print(diagonal_dif(array1, number))

print(difference(array1, number))

print(diagonalsol(array1))