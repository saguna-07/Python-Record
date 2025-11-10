l, u, p, d = 0, 0, 0, 0
s = "R@BB@_0MMMHHH9$"
if (len(s) >= 8):
   for i in s:
       # counting lowercase alphabets
       if (i.islower()):
           l += 1
            # counting uppercase alphabets
       if (i.isupper()):
           u += 1
           # counting digits
       if (i.isdigit()):
           d += 1
           # counting the mentioned special characters
       if (i == '@' or i == '$' or i == '_'):
           p += 1
if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(s)):
   print("Valid Password")
'''elif(l<=0 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
   print("Invalid Password and lower case missing , minimum 1 required  ")
elif(l>=1 and u>=0 and p>=1 and d>=1 and l+p+u+d==len(s)):
   print("Invalid Password and lower case missing , minimum 1 required  ")'''
else:

    if(u == 0):
       print("upper_case is missing")
   elif (l == 0):
       print("lower_case is missing")
   elif(d == 0):
       print('digit is missing')
   elif(p == 0):
       print('symbol is missing')
print("Invalid Password")


