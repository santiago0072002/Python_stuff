# def move_element_to_end(array, target):
#     ltni = len(array) - 1
#     while (array[ltni] == target and ltni > 0):
#         ltni-=1;
#     if (ltni == 0): return array
#     ptr = ltni - 1
#     while (ptr >= 0):
#         print(array)
#         if array[ptr] == target:
#             array[ptr] = array[ltni]
#             array[ltni] = target
#             ltni -= 1
#         else:
#             ltni -= 1
#         ptr  -= 1
#     return array
#     ptr = 0
# # 1 2 3 2 2 2 4 2

def move_element_to_end(array, target):
    arrptr = 0 
    while arrptr < len(array):
		if array[arrptr]==toMove:
			array.append(array[arrptr])
			array.remove(array[arrptr])
			arrptr += 1
		else:
			arrptr += 1
    return array

# this is a living of the land type solution 
def move_element_to_end(array, target):

    for i in range(len(array)):
        if array[i]==target:
            array.append(array[i])
            array.remove(array[i])
        else: 
            i+=1
    return array



a = [ 2, 1, 2, 2, 2, 3, 2, 4]
print(a)
print(move_element_to_end(a, 2))

# 


# rrr
# output 1,3,4,22222 , target for this example is two