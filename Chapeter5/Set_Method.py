###############Set Method###############

# Set Method is used to create a set in Python.

# 1. add(element): Adds an element to the set.
# 2. remove(element): Removes the specified element from the set. Raises KeyError if the element is not found.
# 3. discard(element): Removes the specified element from the set if it exists, does not raise an error if not found.
# 4. pop(): Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
# 5. clear(): Removes all elements from the set, making it empty.
# 6. union(other_set): Returns a new set with elements from both sets.
# 7. intersection(other_set): Returns a new set with elements common to both sets.
# 8. difference(other_set): Returns a new set with elements in the first set but not in the second.


################## Example of Set Methods##################

S = {1, 2, 3, 4, 5, "shubham", 6.5}
print(S, type(S))  # Output: {1, 2, 3, 4, 5, 'shubham', 6.5} <class 'set'>

# 1. add(element)
S.add(7)
print(S)  # Output: {1, 2, 3, 4, 5, 6.5, 7, 'shubham'}

# 2. remove(element)
S.remove(7)
print(S)  # Output: {1, 2, 3, 4, 5, 6.5, 'shubham'}
# 3. discard(element)
S.discard(6.5)
print(S)  # Output: {1, 2, 3, 4, 5, 'shubham'}
# 4. pop()
S.pop()
print(S)  # Output: {2, 3, 4, 5, 'shubham'}
# 5. clear()
S.clear()
print(S)  # Output: set()
# 6. union(other_set)
S1 = {1, 2, 3}
S2 = S.union(S1)
print(S2)  # Output: {1, 2, 3, 4, 5, 6.5, 7, 'shubham'}
# 7. intersection(other_set)
S3 = S.intersection(S1)
print(S3)  # Output: {1, 2, 3}



############## properties of set ###############

# 1. Unordered: Sets are unordered collections, meaning the elements do not have a defined order.
# 2. Unique Elements: Sets automatically remove duplicate elements.
# 3. Mutable: Sets are mutable, allowing you to add or remove elements.
# 4. Heterogeneous: Sets can contain elements of different data types.
# 5. Set cannot contain duplicate values: If you try to add a duplicate element, it will be ignored.
# 6. There is no way to change items in a set.


################ Operations on Sets ###################

