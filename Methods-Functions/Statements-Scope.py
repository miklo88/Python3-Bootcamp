'''
Nested Statements and Scope
'''
x = 25
def printer():
    x = 50
    return x
print(x) # returns 25

# why does 25 return?
# Looks like we're about to start talking about global scope.
'''
LEGB Rule:
L: Local -- Names assigned in any way within a function (def or lambda),
and not declared global in that function.

E: Enclosing function locals -- Names in the local scope of any and all enclosing functions
(def or lambda), from inner to outer.

G: Global (module) -- Names assigned at the top level of a module file,
or declared global in a def within the file.

B: Built-in (Python) -- Names preassigned in the built-in names module:
open, range, SyntaxError
'''
#example of a local variable
# lambda num:num**2
#example of closing function local
#global
name = 'This is a global string'

def greet():
    #enclosing
    name = 'Sammy'
    def hello():
      # local
        print('Hello ' +name)
    hello()

print(greet()) #returns Hello Sammy

x = 50
def func(x):
    # global x
    print(f'X is {x}') #returns X is 50

    #local reassignment
    # x = 200
    x = 'New Value'
    print(f'I just locally changed X to {x}')
# print(func(x)) # I just locally changed X to 200
print(func()) # I just locally changed X to New Value
