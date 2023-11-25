# Exercise 1: Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

# string =input("Enter string: ")
# length = len(string)
# index = length-1
# while index>-1:
#     print(string[index])
#     index-=1

#Exercise 2: Given that fruit is a string, what does fruit[:] mean?

# string = 'fruit'
# print(string[:])

#Exercise 4: There is a string method called count that is similar to
# the function in the previous exercise. Read the documentation of this
# method at:
# https://docs.python.org/library/stdtypes.html#string-methods
# Write an invocation that counts the number of times the letter a occurs
# in “banana”.

string = 'banana'
print(string.count('a'))
