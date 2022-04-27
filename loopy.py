# There are two types of loops in Python: while and for:
# the while loop executes a statement or a set of statements as long as a
# specified boolean condition is true, e.g.:

# The while loop executes  a statement or set of statements as long as a
# specified boolean condition is true, e.g.:

# Example 1
#while True:
#    print("Stuck in an infinite loop.")

# Example 2
#counter = 5
#while counter > 2:
#    print(counter)
#    counter -=  1


# The for loop executes a statements many times;
# It's used to iterate over a sequence (e.g., a list, a dictionary, a tuple,
# or a set - you will learn about them soon) or other objects that are
# iterable( e.g., strings). You can use the for loop to iterate over a
# sequence of numbers using the built-in range function. Look at the example
# below;

# Example 1
#word = "Python"
#for letter in word:
#   print(letter, end="*")
    
# Example 2
#for i in range(1,10):
#    if i % 2 == 0:
#        print(i)

# the break and continue statements to change the flow of a loop.
# break to exit a loop
#text = "OpenEDG Python Institute"
#for letter in text:
#    if letter == "P":
#        break
#    print(letter, end="")
    
# You use continue to skip the current iteration, and continue with the
# next iteration, e.g.
#text = "pyxpyxpyx"
#for letter in text:
#    if letter == "x":
#        continue
#    print(letter, end="")

# The while and for loops can also have an "else" clause in python.
# The else clause executes after the loop finishes its execution as
# long as it has not been terminated by break, e.g.:

# n = 0
# 
# while n != 3:
#     print(n)
#     n += 1
# else:
#     print(n, "else")
#     
# print()
# 
# for i in range(0, 3):
#     print(i)
# else:
#     print(i, "else")

# The range() function generates a sequence of numbers. it accepts
# integers and returns range objects. The syntax of range() looks as
# follows: range(start, stop, step), where:
#    * start is an optional parameter specifying the start number of the
#    sequence (0 by default)
#    * stop is an optional parameter specifying the end of the sequence
#    generated(it is not included)
#      * and step is an optional parameter specifying the difference between
#      the numbers in the sequence(1 by default.)

# Example Code
# for i in range(3):
#     print(i, end= " ") # outputs: 0 1 2

# for i in range(6, 1, -2):
#     print(i, end= " ") # outputs: 6 4 2

# print odd numbers between 0 to 10
# for i in range(1,11):
#     if i % 2 != 0:
#         print(i)

# while loop that prints odd number between 0 to 10
# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x += 1
# pretext = ""
# # for loop print email pretext before @
# for ch in "johnsmith@pythoninstitute.org":
#     if ch == "@":
#         break
#     pretext = ch
#     print(pretext, end="")
  
# for loop to replace 0 with x
# newDigit = ""
# for digit in "0165031806510":
#     if digit == "0":
#         digit = "x"
#         newDigit += digit
#         continue
#     newDigit += digit
# print(newDigit)

# n = 3
# 
# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)

# n = range(4)
# 
# for num in n:
#     print(num - 1)
# else:
#     print(num)

#for i in range(0, 6, 3):
#     print(i)

# The else block in while loop
# n = 3
# 
# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)

# The else block in for loop
n = range(4)

# for num in n:
#     print(num - 1)
# else:
#     print(num)


