##############    Conditionals in Python ####################

# Conditionals म्हणजेच निर्णय घेणे. Python मध्ये, आपण if, elif, else या keywords चा वापर करून conditionals तयार करू शकतो.
# Conditionals allow us to execute certain blocks of code based on specific conditions.


# 1. if statement:
a = int(input("Enter your age: "))
if (a >= 18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#if else statement:
c = int(input("Enter your salary: "))
if (c >= 50000):
    print("You are in the high income group.")
else:
    print("You are in the low income group.")

# 3. elif statement:
b = int(input("Enter your marks: "))
if (b >= 90):
    print("Grade: A")
elif (b >= 80):
    print("Grade: B")
elif (b >= 70):
    print("Grade: C")
else:
    print("Grade: D")
