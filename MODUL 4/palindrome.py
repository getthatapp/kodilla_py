def palindrome(p):
   return p == p[::-1]

p = 'oko'
answer = palindrome(p)

if answer:
    print("TRUE")
else:
    print("FALSE")