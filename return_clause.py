# The effect behaviour of return instruction.
def message(number):
    return
    print("Enter a value: ", number)
    
message(76)
   
# The result behaviour of return instruction.
def boring_function():
    print("'Boredom Mode' ON.")
    return 123

# By default a function return None value as it's result
def message1():
    x= 5

print(message1())

print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")

#  Effects and results: list and functions.
# A list passed as an argument to a function.
def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s
    
print(list_sum([5, 4, 3]))
# print(list_sum(5))

# Effects and results: lists and functions.
# May a list be a function result?
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))


