

###################String in python##################


# String is a sequence of characters
# String is immutable
# String is a collection of characters enclosed in single or double quotes
# String can be created using single quotes, double quotes, or triple quotes
# String can be created using the str() function
# String can be created using the str() constructor

# we can primarily write a string in these three ways.

# 1. Using single quotes
single_quote_string = 'Hello, World!'

# 2. Using double quotes
double_quote_string = "Hello, World!"

# 3. Using triple quotes (for multi-line strings)
triple_quote_string = """Hello,
World!
This is a multi-line string."""


#1) string slicing

# String Slicing म्हणजे string मधून काही भाग (substring) काढण्यासाठी वापरली जाणारी पद्धत.
# String Slicing is a method used to extract a portion (substring) from a string.



# String slicing allows us to access a part of the string

# Syntax: string[start:end:step]
# start: The starting index (inclusive)
# end: The ending index (exclusive)
# step: The step size (optional)

# Example
my_string = "Hello, World!"
print(my_string[0:5])   # Output: Hello
print(my_string[7:12])  # Output: World

print(my_string[1:5:2])  # Output: el

# 1️⃣ [1:5:2] याचा अर्थ:  दर दुसरा character घ्या. 

# start = 1 → index 1 पासून सुरू करा

# end = 5 → index 5 पर्यंत (5 exclusive आहे म्हणजे 5 चा character घेणार नाही)

# step = 2 → दर दुसरा character घ्या






########### Negative Indexing ###########

my_string = "Hello, World!"
print(my_string[-1])   # Output: !
print(my_string[-4:-1])  # Output: orl

print(my_string[::-1])   # Output: !dlroW ,olleH




############## Slicing with skip value ##############

my_string = "Hello, World!"
print(my_string[::2])   # Output: Hlo ol!
print(my_string[1::2])  # Output: el,Wrd
