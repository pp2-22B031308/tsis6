def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False
my_string = "fh,mv"
if is_palindrome(my_string):
    print(my_string, "is a palindrome")
else:
    print(my_string, "is not a palindrome")
