#series in which the num will be the sum of last 2 nums eg:0,1,1,2,3,5,...

n=10
a=0 #1st num of series
b=1 #2nd num of series
print(a)
print(b)
for i in range(3,n+1): #1st 2nums alraedy there 
    c=a+b
    print(c)
    a=b
    b=c
    
