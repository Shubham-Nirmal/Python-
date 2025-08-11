# Dictionary
# A dictionary is a collection of key-value pairs.
# Each key-value pair is separated by a colon (:), and the pairs are enclosed in curly braces ({}).
# This is also used to store data.

d= {} # empty dictionary

marks = {
    "harry": 90,
    "rohan": 80,
    "shubham": 70,
}

print(marks, type(marks))  
# Output: {'harry': 90, 'rohan': 80, 'shubham': 70} <class 'dict'>

print(marks["harry"])  # Output: 90 (accessing value using key)



############## Properties of Dictionary #####################

# 1. Unordered: Dictionaries do not maintain the order of elements.
# 2. Mutable: Dictionaries can be changed after creation, allowing for addition, removal, or modification of key-value pairs.
# 3. Indexing: Dictionaries are indexed by keys, not by numbers like lists or tuples.
# 4. Cannot contain duplicate keys: Each key in a dictionary must be unique.
# 5. Keys must be immutable: Keys can be of any immutable data type, such as strings, numbers, or tuples.
# 6. Values can be of any data type: Values can be of any data type, including lists, tuples, or even other dictionaries.




####################### Dictionary Methods #####################

# 1. keys(): Returns a view object displaying a list of all the keys in the dictionary.
# 2. values(): Returns a view object displaying a list of all the values in the dictionary.
# 3. items(): Returns a view object displaying a list of key-value pairs in the dictionary.
# 4. get(key): Returns the value for the specified key if it exists, otherwise returns None.
# 5. pop(key): Removes the specified key and returns its value. Raises KeyError if the key is not found.
# 6. update(other_dict): Updates the dictionary with key-value pairs from another dictionary.

# 7. clear(): Removes all items from the dictionary, making it empty.
# 8. copy(): Returns a shallow copy of the dictionary.
# 9. fromkeys(seq, value): Creates a new dictionary with keys from the sequence and all values set to the specified value.
# 10. setdefault(key, default): Returns the value of the specified key if it exists, otherwise sets it to the default value and returns that.

############# Example of Dictionary Methods #############

# Example of dictionary methods

# 1. keys()
print(marks.keys())  # Output: dict_keys(['harry', 'rohan', 'shubham'])

# 2. values()
print(marks.values())  # Output: dict_values([90, 80, 70])

# 3. items()
print(marks.items())  # Output: dict_items([('harry', 90), ('rohan', 80), ('shubham', 70)])

# 4. get(key)
print(marks.get("harry"))  # Output: 90
print(marks.get("john"))  # Output: None


print(marks.get("harry2")) # Output: None (key does not exist)
print (marks["harry2"]) # Raises KeyError: 'harry2' (key does not exist)

# 5. pop(key)
print(marks.pop("rohan"))  # Output: 80
print(marks)  # Output: {'harry': 90, 'shubham': 70}


# 6. update(other_dict)
marks.update({"john": 85, "doe": 75})
print(marks)  # Output: {'harry': 90, 'shubham': 70, 'john': 85, 'doe': 75}

# 7. clear()
marks.clear()
print(marks)  # Output: {}

# 8. copy()
marks = {"harry": 90, "rohan": 80, "shubham": 70}
marks_copy = marks.copy()
print(marks_copy)  # Output: {'harry': 90, 'rohan': 80, 'shubham': 70}

# 9. fromkeys(seq, value)
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# 10. setdefault(key, default)
print(marks.setdefault("harry", 100))  # Output: 90
print(marks.setdefault("john", 100))  # Output: 100
