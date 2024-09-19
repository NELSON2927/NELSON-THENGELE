def is_palindrome(s):
    
    s = s.replace(" ", "").lower()
    
    
    return s == s[::-1]


user_input = input("Enter a word or phrase: ")


if is_palindrome(user_input):
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")