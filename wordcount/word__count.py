#!/usr/bin/python

# This import is needed to read from the command line
import sys

if __name__ == "__main__":
  # Functions in Python are defined with 'def' as:
  # def foo(<input>):
  #   <do something>
  #   return <value>

  def count_words(data):
    words = data.split(' ')
    num_words = len(words)
    return num_words

  def count_lines(data):
    lines = data.split('\n')
    for l in lines:
      if not l:
        lines.remove(l)

    return len(lines)

  # sys.argv command returns the command line arguments
  # Use len() to check if the number of arguments is less than two
  # if so, print a usage message and exit the command
  if len(sys.argv) < 2:
    print('Usage: python word__count.pv <file>')
    exit(1)
  
  # The first element of sys.argv will be the filename itself, so: word__count.py, the second will be the user's inputted filename
  filename = sys.argv[1]

  # Open and read the data from the user's filename input
  file = open(filename, 'r')
  data = file.read()
  file.close()

  # Call the previous defined functions to get the words and lines count
  num_words = count_words(data)
  num_lines = count_lines(data)

  print("The number of words is: ", num_words)
  print("The number of lines is: ", num_lines)