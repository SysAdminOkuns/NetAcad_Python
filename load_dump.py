import json

myDict= {
    "Firstname" : "Michael",
    "Lastname" : "Boggs",
    "Role" : "AWS Manager",
    "Organization" : "Perscholas",
    "Duration" : "8yrs"
}
## Using the json.dump method to dump dictionary to a file.
with open('Somefile.txt', 'w+') as f:
    json.dump(myDict, f)

## Using the json.load method to load from a file.
with open('Somefile.txt') as f:
    jsonData= json.load(f)
    
print("{1} is of type {0}".format(type(jsonData), jsonData))
