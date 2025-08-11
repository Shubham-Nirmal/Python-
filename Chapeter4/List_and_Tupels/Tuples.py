########## Tuples IN Python 

# Tuples म्हणजे immutable sequences, म्हणजेच एकदा तयार झाल्यावर त्यांना बदलता येत नाही.
# Tuples are immutable sequences, meaning they cannot be changed once created.

# Tuples is an immutable data type in Python. 


a = () #empty tuple
print(type(a))  # Output: <class 'tuple'>

############### tuples methods #####################
# Tuples have a limited set of methods compared to lists, as they are immutable.


b = (1,21,324,6,5,6,7,8,9,10)  # tuple with multiple elements
print(b.count(6))  # Output: 2 (counts occurrences of 6)

print(b.index(324))  # Output: 2 (index of the first occurrence of 324)

friends = ("Apple", "Banana", "Cherry")
# 1. count() - Returns the number of occurrences of a specified element in the tuple
print(friends.count("Apple"))  # Output: 1 (count of 'Apple')
# 2. index() - Returns the index of the first occurrence of a specified element
print(friends.index("Banana"))  # Output: 1 (index of 'Banana')
# 3. Tuples do not have methods like append(), remove(), or sort() since they are immutable.
