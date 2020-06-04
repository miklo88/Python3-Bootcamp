'''
Variable assignment introduction. Basic variable assignments
'''
a = 5
print(a)

a = 10 
print(a)

print(a + a)
# re-assigning a value
a = a + a
print(a)
# lets find out what data type is a
print(type(a))
# <class 'int'>
b = 30.1
print(b)
print(type(b))
# <class 'float'>

my_income = 100

tax_rate = 0.1

my_taxes = my_income * tax_rate

print(my_taxes)
print(type(my_taxes))
# <class 'float'>

'''
Strings introduction.
Strings are sequences of characters, using the syntax of either single quotes or double quotes:
'hello'
"Hello"
" I don't do that "
-Because strings are ordered sequences it means we can using indexing and slicing to grab sub-sections of the string.
-Indexing notation uses[] notation after the string (or variable assigned the string).
-Indexing allows you to grab a single character from the string.
-Reverse Indexing is available as well.
'''
print('hello')
print("hola")
print('white spaces are included in stings.')
# double spaces
print("I'm on a run")
# a lil print tab formatting # adds a tab 
print('hello \tworld')
#len built in function # does count whitespace.
print(len('I am hungry'))