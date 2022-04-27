from os import system as sys
from time import sleep
# var = 1
# while var < 10:
#     print("#")
#     var = var << 1


# i = 0
# while i <= 5:
#     i += 1
#     if i % 2 == 0:
#         break
#     print("*")

# my_list = [1,2,3,4]
# print(my_list[-3:-2])

# for i in range(1):
#     print("#")
# else:
#     print("#")
#     
# def message(number):
#      sys('cls')
#      print("You entered", number)
#      
# def getValue():
#     print("Please, enter a number: ")
#     return int(input())
# 
# def total(x, y, z):
#     sys('cls')
#     print(f"Total of {x} + {y} + {z} is equal to",x + y + z)
# 
# 
# a = getValue()
# message(a)
# b = getValue()
# message(b)
# c = getValue()
# message(c)
# 
# total(a, b, c)

# Understanding variable shadowing(x shadow with variable in a function)
# def message(number):
#     print(id(number))
# #     print("Enter a number: ", number)
#     
# number = 1234
# message(1)
# print(id(number))

# def groceryList(what, number):
#     print("Entered", what, "no.", number)
#     
# groceryList("apple", 11)
# groceryList("Grapes", 28)
# groceryList("Bananas", 20)

# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
#
# FirstName first then LastName (Positional parameter or argument)
# introduction("Luke", "Skywalker")
# introduction("Jesse", "Quick")
# introduction("Clark", "Kent")

# Python offers another convention for passing arguments,
# where the meaning of the argument is dictated by its name,
# not by its position - it's called keyword argument passing.
#
# LastName first then FirstName (Keyword arguments)
# introduction(last_name="Skywalker", first_name="Luke")
# introduction("Quick", "Jesse")
# introduction("Kent", "Clark")

# Of course, you mustn't use a non-existent parameter name.
# TypeError: introduction() got an unexpected keyword argument 'surname'
# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
# 
# introduction(surname="Skywalker", first_name="Luke")

# Mixing positional and keyword arguments, however obey one rule
# You can mix both fashions if you want -
# there is only one unbreakable rule:
# you have to put positional arguments before keyword arguments.
# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)

# Call the adding function here.
# adding(3, c = 1, b = 2)
# adding(3, a = 1, b = 2)
# adding(4, 3, c = 2)

# Default or predefined values in parameter
# It happens at times that a particular parameter's values are in
# use more often than others. Such arguments may have their
# default (predefined) values taken into consideration
# when their corresponding arguments have been omitted.
# 
# They say that the most popular English last name is Smith.
# Let's try to take this into account.
# def introduction(first_name, last_name="Smith"):
#     print("Hello, my name is", first_name, last_name)
#     
# # introduction("James", "Doe")
# # introduction("Henry")
# # introduction(first_name="William")
# 
# def introduction(first_name="John", last_name="Smith"):
#     print("Hello, my name is", first_name, last_name)
# 
# # introduction()
# introduction(last_name="Hopkins")
# 
# non-default argument(c) follows default argument(b=2)
# def add_numbers(a, b=2 , c):
#     print(a + b + c)
# 
# add_numbers(a=3, c=2)

# The return instruction
# def greeting(name):
#     print("Hello", name)
#     return
# 
# myName = greeting
# 
# myName("Nosa")

# you can use it to terminate a function's activities on demand,
# before the control reaches the function's last line.

# def happy_new_year(wishes = True):
#     print("Three...")
#     sleep(2)
#     sys('cls')
#     print("Two...")
#     sleep(2)
#     sys('cls')
#     print("one...")
#     sleep(2)
#     sys('cls')
#     if not wishes:
#         return
#     print("Happy New Year!")
#     
# happy_new_year(False)

# The return instruction with a value from an expression.
# def boring_function():
#     return 123
# 
# x = boring_function()
# 
# print("The boring_function has returned its result. It's:", x)

# Don't forget this: if a function doesn't return a certain value
# using a return expression clause,
# it is assumed that it implicitly returns None.
# value = None
# if value is None:
#     print("Sorry, you don't carry any value")

# Effects and results: list and functions
# May list be passed to a function, Yes!
# def list_sum(lst):
#     s = 0
#     
#     for elem in lst:
#         s += elem
#     
#     return s
#     
# print(list_sum([x for x in range(10)]))
# print(list_sum(5))

# Effects and results: lists and functions
# May a list be a function result? Yes, of course!
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))

    
    