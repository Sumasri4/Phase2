rev=0
n=1234
n1=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if rev==n1:
    print("palindrome")
else:
    print("not")
    
