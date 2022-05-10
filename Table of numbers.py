def tables(x):
    for i in range(1,11):
        print(x,"x", i, "=", x*i)

x = int(input("Enter the number : "))
print(tables(x))