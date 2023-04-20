def isPalindrome(s): 
   return s == s[::-1]
s = "dev"

ans = isPalindrome(s) 
if ans:
     print("this string is palindrome") 
else:
     print("this string is not palindrome")