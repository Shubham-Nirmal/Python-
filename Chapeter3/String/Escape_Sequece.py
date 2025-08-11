########## Escape Sequence in Python ##########


#Escape Sequence म्हणजे string मध्ये काही special characters वापरण्यासाठी वापरली जाणारी पद्धत.

# Escape Sequence is a method used to include special characters in a string.

# Most important escape sequences for interviews:
# \n  - Newline (moves to the next line)
# \t  - Tab (adds a horizontal tab space)
# \\  - Backslash (adds a backslash character)
# \'  - Single quote (adds a single quote)
# \"  - Double quote (adds a double quote)
# \r  - Carriage return (moves cursor to start of line)
# \b  - Backspace (removes previous character)
# \0  - Null character (represents nothing)
# \uxxxx / \Uxxxxxxxx - Unicode characters (for special symbols)
# \xhh - Hexadecimal value (for special characters)
# These are commonly asked and used in Python interviews.

 
# Example of Escape Sequences

A = "shubham is good boy \n he is also a good coder"
print(A)  

B = "shubham is a good boy \\ he is also a good coder"
print(B)