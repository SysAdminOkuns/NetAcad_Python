## Creating and writing to a none existing file.
f = open("first.txt", 'w')
f.write("Hello World\n")
f.write("Hello, Python!")
f.close()

# f= open("first.txt")
# myStr= f.read()
# print(myStr)

with open("first.txt", 'a') as f:
    f.write("\nHello, Travis and Echo for a wonderful class.")
  

with open("first.txt") as f:
    mystr= f.read()
    print(mystr)
    