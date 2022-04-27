def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# Call the adding function here.
adding(1,2,3)
adding(c = 1, a = 2, b = 3)
adding(3, c = 1, b = 2)
# The invocation below flags a TypeError
# adding(3, a = 1, b = 2)
adding(4, 3, c = 2)