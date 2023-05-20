def Palindrome(n):
  return n == n[::-1]


n = '12345'
a = Palindrome(n)

if a:
  print("pallindrome")
else:
  print("not an pallindrome")