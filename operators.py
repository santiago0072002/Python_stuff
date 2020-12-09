#https://www.w3schools.com/python/python_operators.asp
#Python Assignment Operators
# Assignment operators are used to assign values to variables:
"""

Operator	Example	    Same As	
=	        x = 5	    x = 5	
+=	        x += 3	    x = x + 3	
-=	        x -= 3	    x = x - 3	
*=	        x *= 3	    x = x * 3	
/=	        x /= 3	    x = x / 3	
%=	        x %= 3	    x = x % 3	
//=	        x //= 3	    x = x // 3	
**=	        x **= 3	    x = x ** 3	
&=	        x &= 3	    x = x & 3	
|=	        x |= 3	    x = x | 3	
^=      	x ^= 3	    x = x ^ 3	
>>=	        x >>= 3	    x = x >> 3	
<<=	        x <<= 3	    x = x << 3
"""
# Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:
"""
Operator	Name	        Example	
+	        Addition	    x + y	
-	        Subtraction	    x - y	
*	        Multiplication	x * y	
/	        Division	    x / y	
%	        Modulus	        x % y	
**	        Exponentiation	x ** y	
//	        Floor division	x // y

"""

# Comparison Operators
""" 
Operator	Name	                            Example
==	        Equal	                            x == y	
!=	        Not equal	                        x != y	
>	        Greater than	                    x > y	
<	        Less than	                        x < y	
>=	        Greater than or equal to	        x >= y	
<=	        Less than or equal to	            x <= y

"""
"""
Operator	            Description	                                                    Example	
and 	                  Returns True if both statements are true              	    x < 5 and  x < 10	
or	                      Returns True if one of the statements is true	                x < 5 or x < 4	
not	                      Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)

"""
# Operator	    Description	                                                        Example	
# is 	        Returns True if both variables are the same object	                x is y	
# is not	    Returns True if both variables are not the same object	            x is not y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

""" Operator	        Description	                                                                             Example
in 	                    Returns True if a sequence with the specified value is present in the object	         x in y
not in	                Returns True if a sequence with the specified value is not present in the object	     x not in y

"""

x = 'Hello world'
y = {1:'a',2:'b'}# this is a dictionary 

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y) # is the value a in the key index y

"""
From the above lines
Here, 'H' is in x but 'hello' is not present in x (remember, Python is case sensitive).
Similarly, 1 is key and 'a' is the value in dictionary y. Hence, 'a' in y returns False.
"""

""" 
Bitwise operators are used to compare (binary) numbers:

Operator	Name	                Description
& 	        AND	                    Sets each bit to 1 if both bits are 1
|	        OR	                    Sets each bit to 1 if one of two bits is 1
 ^	        XOR	                    Sets each bit to 1 if only one of two bits is 1
~ 	        NOT	                    Inverts all the bits
<<          Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

"""