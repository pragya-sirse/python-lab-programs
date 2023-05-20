
def Palindrome(s):
  return s == s[::-1]


s = "python"
a = Palindrome(s)

if a:
  print("pallindrome")
else:
  print("not an pallindrome")