'''
While Loops
They will continue to execute a block of code while a condition is true
Ex. WHILE my pool is not full, keep filling my pool with water.
Or WHILE my dogs are still hungry, keep feeding my dogs.

syntax of a while loop
while some_boolean_condition:
    #do something
else:
    # do something different when its no longer true

'''

x = 0
while x < 5:
    print(f'The current value of x is {x}')

    x += 1
# the while loop keeps running until the value matches 5. so you return 0,1,2,3,4
else:
    print(f'{x} is not less than 5') # when values iterates to 5 it prints this statement.

'''
Break, Continue, Pass
We can use break, continue, and pass statements in our loops to add additional functionality 
for various cases. The three statements are defined by:
    break: Breaks out of the current closest enclosing loop.
    continue: Goes to the top of the closest enclosing loop.
    pass: Does nothing at all.
'''
#pass
x = [1,2,3]
for item in x:
    #comment
    pass
print('end of my script')

#continue
mystring = 'Adrian'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter) #returns Adrin - no "a" skips, continues over 'a'

#break
mystring = 'Adrian'
for letter in mystring:
    if letter == 'a':
        break
    print(letter) # returns Adri then breaks the loop when 'a' value is met

x = 0 
while x < 5:
    if x == 2:
        break # returns 0,1 then breaks the loop when '2' value is met
    print(x)
    x += 1
