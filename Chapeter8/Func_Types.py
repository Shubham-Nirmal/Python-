############## types of function #############
#1. Built-in Functions
#2. User Defined Functions
#3. Lambda Functions


############## Built-in Functions #############
# Built-in functions are functions that are already defined in Python.
# These functions are built into the Python language and are available to use without having to define them.

#example of built-in function

print(abs(-5))
print(len("Hello World"))

############## User Defined Functions #############
#User defined functions are functions that are defined by the programmer.
#These functions are defined using the def keyword followed by the function name and a set of parentheses.

#example of user defined function
def add(a, b):
    c = a + b
    return c
print(add(2, 3))