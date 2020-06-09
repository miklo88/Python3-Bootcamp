'''
Table of Comparison Operators
In the table below, a=3 and b=4.

Operator	Description	Example
==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
!=	If values of two operands are not equal, then condition becomes true.	(a != b) is true
>	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
<	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
>=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
<=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.

'''
# simple comparisons with different data types.

# print(2==2) # True
# print(2==1) # False
# print('hello'=='bye') # False
# print('hello'=='Hello') # False
# print(3 != 3) # False
# print(3 != 2) # True
# print(3 > 2) # True
# print(3 < 2) # False
# print(3 <= 5) # True
# print(10 >= 5) # False

'''
Chaining Comparison Operators in Python with Logical Operators
'''
print(1 < 2 < 3) # True
print(1 < 2 > 3) # False
print(1 < 2 and 2 > 3) # False with the and keyword
print(1 < 2 and 2 < 3) # True with the and keyword
print('h' == 'h' and 2 != 3) # True
print(1 == 1 or 2 == 2) #True or keyword. as long as one or the other is true it'll return true
print(1 == 1 or 2 == 3) #True or keyword. the same as above applies for false
#not keyword. another way of saying is one equal to this, but not equal to this
print(1 != 1) 
print(not 400 == 5000)
