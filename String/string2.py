# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

def verbing(s):

  if len(s) >= 3:
    if s[-3:] == 'ing':
      result = s + 'ly'
    else: result = s + 'ing'
  else: result = s

  return result


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

def not_bad(s):

  findNot = s.find('not')
  findBad = s.find('bad')

  if findNot != -1 and findBad != -1 and findBad > findNot:
    result = s[:findNot] + 'good' + s[findBad + 3:]
  else: result = s

  return result


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

def front_back(a, b):

  if len(a) % 2 == 0:
    half = int(len(a) / 2)
    aFront = a[:half]
    aBack = a[half:]
  else:
    half = int(len(a) / 2 + 1)
    aFront = a[:half]
    aBack = a[half:]

  if len(b) % 2 == 0:
      half = int(len(b) / 2)
      bFront = b[:half]
      bBack = b[half:]
  else:
      half = int(len(b) / 2 + 1)
      bFront = b[:half]
      bBack = b[half:]

  return aFront + bFront + aBack + bBack
  
# TODO: find a better way to solve this...


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print (f'{prefix} got: {got} expected: {expected}')


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.

def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

# Call main function (run the program)
main()