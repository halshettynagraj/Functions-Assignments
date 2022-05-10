#list
def multlist(x):
    result =  1
    for i in x:
        result = result * i
    return result

x = [2,5,6,10]
print(multlist(x))

#tuple
def multtuple(x):
    result =  1
    for i in x:
        result = result * i
    return result

x = (2,5,6,10)
print(multtuple(x))

#Set
def multset(x):
    result =  1
    for i in x:
        result = result * i
    return result

x = {2,5,6,10}
print(multset(x))

