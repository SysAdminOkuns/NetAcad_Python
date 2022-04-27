import json

# Using the json.loads function
myDictString= '{"foo" : "bar"}'
myDict = json.loads(myDictString)
print("{1} is of type {0}".format(type(myDict), myDict))

# Using the json.dumps function returns string type
myStr= json.dumps(myDict)
print("{1}  is of type {0}".format(type(myStr),myStr))





















