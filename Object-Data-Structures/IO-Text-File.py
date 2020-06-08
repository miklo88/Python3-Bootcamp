'''
creating a text file
'''
print('Creating A File')
# Hello this is a text file
# this is the second line
# this is the third line

# Quicknotes
# Open/Create a file - 
myFile = open('about.txt', 'w')

# print(myFile)
# Get some info - 
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('Hello this is a text file, ')
myFile.write('this is the second line, ')
myFile.close()

# Append to file
myFile = open('about.txt', 'a')
myFile.write('this is the third line')
myFile.close() 

# Read from file - allows you to grab everything from one giant string.
myFile = open('about.txt', 'r+')
# text = myFile.read() # brings back a string
text = myFile.readlines() # brings back a list of data

print(text)

# Creating new file to work on.
# newFile = open('py_json.py', 'w')

#File Locations
# If want to open files at another location on your computer, simply pass in the entire file path.

#another high speed way of opening and closing a file
with open('about.txt') as new_file:
    text = new_file.readlines()
print(text)

'''
More Reading, Writing, Appending Modes
mode='r' is read only
mode='w' is write only (will overwrite files or create new!)
mode='a' is append only (will add on to files)
mode='r+' is reading and writing 
mode='w+' is writing and reading (Overwrites existing files or creates a new file!)
'''

with open('second.txt', 'w') as f:
    f.write('\nOne on first,\nTwo on second,\nThree on third')
    #Same as below. a lot faster no?
# anothaFile = open('second.txt', 'w')
# anothaFile.write('One on first,\ntwo on second,\nthree on third')
# anothaFile.close()
# print(anothaFile)
with open('second.txt', mode='a') as f:
    f.write('\nFour on fourth')
with open('second.txt', mode='r') as f:
    print(f.read())
# another example
with open('abcdefghijk.txt', mode='w') as f:
    f.write('I created this random file')
with open('abcdefghijk.txt', mode='a') as f:
    f.write('\nThis is an example of how python based on the mode will create the file no matter its title.')
with open('abcdefghijk.txt', mode='r') as f:
    print(f.read())

