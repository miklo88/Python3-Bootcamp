Objects and Data Structures Assessment Test
Test your knowledge.
Answer the following questions

Write a brief description of all the following Object Types and Data Structures we've learned about:

Numbers: Numbers are integers or floats. the only place this gets spicy is in integers which are whole numbers lik 1, 2, 3, 4 and floats are decimal places such as 3.14, .33, .25, 100.125. These different numbers do have significant meaning in working with them as data.

Strings: Strings in python can be integers, and characters. Mainly used for text but are consistant with assigning value to a variable. example name = 'Carl Redding'. Various methods come with strings. They are immutable data types.

Lists: Just like arrays in javascript. lists are identifiable with the [] brackets. These are mutable little pieces of data which usually involve the slice, pop etc methods. They can contain all data types as strings, integers functions, booleans etc.

Tuples: Immutable data! I as a beginner in the land of python will not be using it that much. Later on it will be good practice for data-integrity. Besides that inside a tuple you can have integers, strings, or lists. Easily identified with the ().

Dictionaries: Just like objects in javascript. Dictionaries contain lists, integers, strings. The big thing to remeber here is that dictionaries work in key value pairs. so key1: value1. ALSO dictionaries can contain dictionaries and identifiable with {} syntax.

Numbers
PEDMAS
Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25
Divide(/) Multiply(*) Add(+) Subtract(-) Exponent(**)
Simple equation form of 20**2 then dividing that number by 5. Then multiplying it by 2 in which i subtract 90 and add 30.25 to get 100.25
(20\*\*2) #400
(400/5) #80.0
(80*2) #160
(160-90) #70
(70+30.25) #100.25
In [print(20**2 /5 *2 -90 +30.25)]: # returns 100.25

Answer these 3 questions without typing code. Then type code to check your answer.

What is the value of the expression 4 \* (6 + 5) # answer 44 # code print(4 _ (6 + 5))
What is the value of the expression 4 \* 6 + 5 # answer 29 # code print(4 _ 6 + 5)

What is the value of the expression 4 + 6 \* 5 # answer 34 # code print(4 + 6 \* 5)
In [ ]:

What is the type of the result of the expression 3 + 1.5 + 4?
data type will be int. but it is a floating type number because of the decimal.

What would you use to find a number’s square root, as well as its square? # answer using pythons exponent number.

# Square root: .sqrt()

    # answer 30\*\*2 = 900

# Square:

    # answer 30\*\*2 = 900 same as above

Strings
Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
In [ ]:
s = 'hello'

# Print out 'e' using indexing

    # answer s[4]

Reverse the string 'hello' using slicing:

In [ ]:
s ='hello'

# Reverse the string using slicing

    # answer s[::-1]

Given the string hello, give two methods of producing the letter 'o' using indexing.
s ='hello'

# Print out the 'o'

# Method 1:

    # answer s[4]

# Method 2:

    # answer s[-1]

Lists
Build this list [0,0,0] two separate ways.

# Method 1:

    # answer list = [0,0,0]

# Method 2:

    # answer list = ['0', '0', '0']

Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']] # answer list3[2][2] = 'goodbye'
print(list3) = # returns [1, 2, [3, 4, 'goodbye']]

Sort the list below:
list4 = [5,3,4,6,1] # answer list4.sort() # returns [1, 3, 4, 5, 6]

Dictionaries
Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}

# Grab 'hello'

    # answer print(d['simple_key']) # returns 'hello'

d = {'k1':{'k2':'hello'}}

# Grab 'hello'

    #answer print(d['k1']['k2']) # returns 'hello'

# Getting a little tricker

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello # answer print(d['k1'][0]['nest_key'][1])

# This will be hard and annoying!

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]} # answer - print(d['k1'][2]['k2'][1]['tough'][2]) # returns ['hello']

Can you sort a dictionary? Why or why not? No. Dictionaries are inherently orderless. unlike lists and tuples

Tuples
What is the major difference between tuples and lists?
Tuples are immutable and lists are mutable

How do you create a tuple?
t = (1,2,3) with your variable you enclose your data in a parenthesis. ()

Sets
What is unique about a set? Sets are great for grabbing unique data!

Use a set to find the unique values of the list below:

In [ ]:
list5 = [1,2,2,33,4,4,11,22,3,3,2] # answer print(set(list5)) # returns {1, 2, 33, 4, 3, 11, 22}

Booleans
For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.

Operator Description Example
== If the values of two operands are equal, then the condition becomes true. (a == b) is not true.
!= If values of two operands are not equal, then condition becomes true. (a != b) is true.

>     If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
>
> < If the value of left operand is less than the value of right operand, then condition becomes true. (a < b) is true.
> = If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. (a >= b) is not true.
> <= If the value of left operand is less than or equal to the value of right operand, then condition becomes true. (a <= b) is true.
> What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# Answer before running cell

2 > 3 (not true)

# Answer before running cell

3 <= 2 (not true)

# Answer before running cell

3 == 2.0 (not true)

# Answer before running cell

3.0 == 3 (true)

# Answer before running cell

4\*\*0.5 != 2 (not true)

Final Question: What is the boolean output of the cell block below?

# two nested lists

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?

#False, the first index of l_one in its nested list is 3. the key's value in l_two is 4
l_one[2][0] >= l_two[2]['k1']
Great Job on your first assessment!
