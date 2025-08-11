############# String Functions #############


# String functions म्हणजे string वर काम करण्यासाठी Python मध्ये आधीपासून तयार असलेल्या (built-in) methods.
#String functions are built-in methods in Python for working with strings.





# String functions म्हणजे string वर काम करण्यासाठी Python मध्ये आधीपासून तयार असलेल्या (built-in) methods.



name = "Shubham Bhau"
print(len(name))  # Output: 12 (length of the string)

# 1. lower() - Converts the string to lowercase
print(name.lower())  # Output: shubham bhau

# 2. upper() - Converts the string to uppercase
print(name.upper())  # Output: SHUBHAM BHAU

# 3. strip() - Removes leading and trailing whitespace
name_with_spaces = "   Shubham Bhau   "
print(name_with_spaces.strip())  # Output: "Shubham Bhau"

# 4. replace() - Replaces a substring with another substring
print(name.replace("Bhau", "Kumar"))  # Output: Shubham Kumar

# 5. split() - Splits the string into a list of substrings
print(name.split(" "))  # Output: ['Shubham', 'Bhau']

# 6. join() - Joins a list of strings into a single string
name_list = ['Shubham', 'Bhau']
print(" ".join(name_list))  # Output: "Shubham Bhau"
