#!/usr/bin/python

# Open the test file, hard coded with the file path
file = open('word_test.txt', 'r')
# 'r' is the selected mode of opening, meaning read-only
# Could also have specified 'w' for write, or 'a' for append, etc...

# After opening the file read its contents into a new variable
data = file.read()
# Then close the open file
file.close()

# Then finally print the file contents
print(data)