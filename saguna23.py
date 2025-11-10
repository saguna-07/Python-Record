l,u,p,d=0,0,0,0
s="R@m@_f0rtu9e$"
if(len(s)>=8):
    for i in s:
        if (i.islower()):
            l+=1
        if (i.isupper()):
            u+=1
        if (i.isdigit()):
            d+=1
        if (i=='@' or i=='$' or i=='_'):
            p+=1
        if (l>=1and u>=1 and p>=1and d>=1and l+p+u+d==len(s)):
            print('valid password')
        else:
             if(u == 0):
                print('upper_case is missing')
             elif(l == 0):
                print('lower_case is missing')
             if(d == 0):
                print('digit is missing')
             if(p == 0):
                print('symbol is missing')
                print("Invalid Password")









