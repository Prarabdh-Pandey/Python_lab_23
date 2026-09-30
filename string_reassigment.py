# write a function change_string(s) that tries to replace the first character of the srting with "X".
# call this function and check whether the original string chnages outside the function.

def change_string(s):
    s = "X" + s[1:]
    print("inside function :",s)

string = input("Enter a string: ")

print("Before function call:", string)

change_string(string)

print("After function call:", string)