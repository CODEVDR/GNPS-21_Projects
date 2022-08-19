#3
def palindrome(n):
   if n==n[::-1]:
      return f"{n} is A Palindrome"
   else:
      return f"{n} is not A Palindrome"

print(palindrome(input("Enter a Number to check it is palindrome or not")))
