str_name = str(input("Enter the input string : "))
def Palindrome(str_name):
    return str_name == str_name[::-1]
 
word = Palindrome(str_name)
if word:
    print("Yes")
else:
    print("No")