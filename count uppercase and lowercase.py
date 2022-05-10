# Uppercase
def letters(x):
    return [char for char in x if char.isupper()]
    

x = input("Enter any words : ")
print(len(letters(x)))
print(letters(x))

#LowerCase
def letters(x):
    return [char for char in x if char.islower()]

x = input("Enter any words : ")
print(len(letters(x)))
print(letters(x))


