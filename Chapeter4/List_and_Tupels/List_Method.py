
################list methods##################

# List Methods म्हणजे List वर काम करण्यासाठी Python मध्ये दिलेल्या ready-made functions.

# List Methods are ready-made functions provided in Python for working with Lists.


# List Methods म्हणजे List वर काम करण्यासाठी Python मध्ये दिलेल्या ready-made functions.

friends = ["Apple", "Banana", "Cherry", "Date"]
# 1. append() - Adds an element to the end of the list
friends.append("Elderberry")
print(friends)  # Output: ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

# 2. insert() - Inserts an element at a specific index
friends.insert(1, "Blueberry")
print(friends)  # Output: ['Apple', 'Blueberry', 'Banana', 'Cherry', 'Date', 'Elderberry']

# 3. remove() - Removes the first occurrence of an element
friends.remove("Cherry")
print(friends)  # Output: ['Apple', 'Blueberry', 'Banana', 'Date', 'Elderberry']

# 4. pop() - Removes and returns the last element (or an element at a specific index)
last_friend = friends.pop()
print(last_friend)  # Output: Elderberry
print(friends)  # Output: ['Apple', 'Blueberry', 'Banana', 'Date']

# 5. sort() - Sorts the list in ascending order
friends.sort()
print(friends)  # Output: ['Apple', 'Banana', 'Blueberry', 'Date']

# 6. reverse() - Reverses the order of the list
friends.reverse()
print(friends)  # Output: ['Date', 'Blueberry', 'Banana', 'Apple']

# 7. index() - Returns the index of the first occurrence of an element
print(friends.index("Banana"))  # Output: 2 (index of 'Banana')

# 8. count() - Returns the number of occurrences of an element
print(friends.count("Apple"))  # Output: 1 (count of 'Apple')

# 9. clear() - Removes all elements from the list
friends.clear()
print(friends)  # Output: []

# 10. copy() - Returns a shallow copy of the list

friends = ["Apple", "Banana", "Cherry"]
friends_copy = friends.copy()
print(friends_copy)  # Output: ['Apple', 'Banana', 'Cherry']

# 11. extend() - Extends the list by appending elements from another iterable (like a list)
more_fruits = ["Fig", "Grape"]
friends.extend(more_fruits)
print(friends)  # Output: ['Apple', 'Banana', 'Cherry', 'Fig', 'Grape']

# 12. count() - Returns the number of occurrences of a specified element in the list
print(friends.count("Apple"))  # Output: 1 (count of 'Apple')

# 13. copy() - Returns a shallow copy of the list
friends_copy = friends.copy()
print(friends_copy)  # Output: ['Apple', 'Banana', 'Cherry', 'Fig', 'Grape']

# 14. index() - Returns the index of the first occurrence of a specified element
print(friends.index("Banana"))  # Output: 1 (index of 'Banana')

# 15. clear() - Removes all elements from the list
friends.clear()
print(friends)  # Output: []

# 16. reverse() - Reverses the order of the elements in the list
friends = ["Apple", "Banana", "Cherry"]
friends.reverse()
print(friends)  # Output: ['Cherry', 'Banana', 'Apple']
