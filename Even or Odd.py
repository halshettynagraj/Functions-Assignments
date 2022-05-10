def status(x):
    if x%2 == 0:
        return "The Number is Even"
    else :
        return "The Number is Odd"

x = int(input("Enter the Num : "))
print(status(x))