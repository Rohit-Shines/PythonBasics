import json


####### JSON to python
# Some JSON data :
x =  '{ "name":"John", "age":30, "city":"New York"}' # parse x:
y = json.loads(x) # If you have a JSON string, you can parse it by using the json.loads() method.
# the result is a Python dictionary:
print(y["age"]) # 30


##### a Python object (dict): to JSON
x = { "name": "John", "age": 30, "city": "New York" }
y = json.dumps(x) # convert into JSON:
print(y) # the result is a JSON string:



## Convert all types of Python objects into JSON strings, and print the values:
import json

print(json.dumps({"name": "John", "age": 30})) # set
print(json.dumps(["apple", "bananas"])) # list
print(json.dumps(("apple", "bananas"))) # tuple
print(json.dumps("hello")) # string
print(json.dumps(42)) # int
print(json.dumps(31.76)) # float
print(json.dumps(True)) # boolean
print(json.dumps(False)) # boolean
print(json.dumps(None)) # null # none data type

###### The json.dumps() method has parameters to make it easier to read the result:######
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". "," = "))) # . to sperate words, = to assign key values
print(json.dumps(x, indent=4, sort_keys=True)) # will sort things