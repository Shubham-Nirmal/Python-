# Check the type of the variables assigned using input () function

a = input("Enter a value for a: ")
b = int(input("Enter a value for b: "))
c = float(input("Enter a value for c: "))
d = str(input("Enter a value for d: "))

print ("You entered:", a, "and", b, "and", c, "and", d)
print ("The type of a is:", type(a))
print ("The type of b is:", type(b))
print ("The type of c is:", type(c))
print ("The type of d is:", type(d))