############### function #############

# A function is a group of statements that performs a specific task.
# A function is a block of code that can be called multiple times.

# When a program gets bigger in size and complexity, it gets difficult to keep track of which piece of code is doing what.
# A function can be reused multiple times in a program.

###################### Syntax of a function ################

# def function_name():
#     function body
#     print("Hello World")

############### function call #############
# Whenever we want to call a function, we put the function name followed by parentheses.
# function_name()

######### function definition #############

def avg():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = (a + b) / 2
    print("The average is:", c)

# Function calls
avg()
avg()
avg()


