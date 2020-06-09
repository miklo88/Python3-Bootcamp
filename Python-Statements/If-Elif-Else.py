'''
Control Flow
Often only want certain code to execute when a particular condition has been met.
Example. If my dog is hungry (some condition), then I will feed the dog (some action).
Keywords
- If
- Elif 
- Else
the indentation in python code is what sets it apart from other languages.

if some_condition:
    # execute some code
elif some_other_condition:
    # do something different
else: 
    # do something else
'''

# if True:
#     print('Its true')
# variable passing boolean example
hungry = True
if hungry:
    print('FEED THE BABY')
else:
    print('Im not hungry')

# stacking conditionals and logic
#loc = 'Bank'
loc = 'Game'

if loc == 'Auto Shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'Store':
    print('Welcome to the store!')
else:
    print('I dont know much')

name = 'Carlitos'

if name == 'Frankie':
    print('Hello Frankie')
elif name == 'Carlitos':
    print('Hola Carlitos')
else:
    print('What is your name?')