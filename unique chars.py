

def unique(n): 
    uniqchar = []

    for char in n:
        if char not in uniqchar:
            uniqchar += char.lower()

    print("The list of unique characters is: ", uniqchar)

A = unique(input("enter string : "))

#using for loop

word = input("Enter a string : ")

uniqchar = []

for char in word:
    if char not in uniqchar:
        uniqchar += char.lower()

print("The list of unique characters is: ", uniqchar)