# Write a program to fill in a letter template given below with name add date .  


letter = '''Dear <|Name|>,

you are selected!

Date: <|Date|>'''


print( letter.replace("<|Name|>", "Shubham").replace("<|Date|>", "26/10/2023") )