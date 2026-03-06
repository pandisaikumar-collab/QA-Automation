def check_palindrome(string):
    return string == string[::-1] # reverse the string and compare (:: start-end-step)

s1 = check_palindrome("madam")
if s1 == True:
    print("palindrome.")
else:
    print("not a palindrome.")
