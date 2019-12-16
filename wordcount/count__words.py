#!/usr/bin/python

file = open('word_test.txt', 'r')
data = file.read()
file.close()

words = data.split(" ")
# Split the file contents by spaces, to get every word in it, then print
print('The words in this file are: ' + str(words))

num_words = len(words)
# Use the len() function to return the length of a list (words) to get the word count, then print
print('The number of words in this file is: ' + str(num_words))

lines = data.split('\n')
# Split the file contents by \n to get each individual line, then print
print('The separate lines in this file are: ' + str(lines))

# use the len() function again to get the number of lines there are
print('The number of lines, including empty lines, is: ' + str(len(lines)))

# To remove the empty lines from the array list, use a for loop
# the NOT keyword automatically checks for emptiness, if the current entry is empty then it gets
# removed from the array 'lines'

for l in lines:
  if not l:
    lines.remove(l)

print('The number of non-empty lines only is: ' + str(len(lines)))
