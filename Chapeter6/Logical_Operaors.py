# Logical Operators in Python

# Logical operators म्हणजेच तार्किक operators. Python मध्ये, आपण and, or, not या operators चा वापर करून दोन किंवा अधिक conditions चा संबंध तपासू शकतो.

# 1. And (&&) operator:
a = 10
b = 20
if (a < b and b > 15):
    print("Both conditions are true.")
else:
    print("At least one condition is false.")

# 2. Or (||) operator:
c = 30
d = 25
if (c > d or c < 20):
    print("At least one condition is true.")
else:
    print("Both conditions are false.")

# 3. Not (!) operator:
e = 40
if not (e < 30):
    print("Condition is true.")
else:
    print("Condition is false.")
