'''
Errors are boudn to hapen in your code.
Especially when someone else ends up using it in an unexpected way.
We can use error handling to attempt to plan for possible errors.

Keywords:
try: This is the block of code to be attempted (may lead to error)
except: Block of code will execute in case there is an error in try block.
finally: A final block of code to be executed, regardless of an error.
'''

# def add(n1, n2):
#     print(n1+n2)

# # add(10, 20)
# print(add(10, 20))

# try:
#     # want to attempt this code'
#     # may have an error
#     result = 10 + 10
# except:
#     print("Hey it look's like you aren't adding correctly.")
# else:
#     print("add went well")
#     print(result)

# try:
#     f = open('testfile', 'w')
#     f.write("write a test line")
# except TypeError:
#     print("There was a Type Error.")
# except OSError:
#     print('There was an OS Error')
# finally:
#     print("I always run.")

# def ask_for_int():
#     while True:
#         try:
#             result = int(input("Provide thy numba: "))
#         except:
#             print("Hey now, thats not a number.")
#             continue
#         else:
#             print("Correct Integer")
#             break
#         finally:
#             print("Finally out")
#             print('I never stop running.')
#             # continue

# print(ask_for_int())
# /////////// HOMEWORK FILE
'''
Problem 1. Handle the exception thrown by the code below by using try and except blocks.
for i in ['a','b','c']:
    print(i**2)

'''

'''
Problem 2.
Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print('All Done.')
'''

'''
Problem 3.
Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    pass
ask()
// return
Input an integer: null
An error occurred! Please try again!
Input an integer: 2
Thank you, your number squared is:  4
'''
# /////////// HOMEWORK FILE
