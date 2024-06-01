n=21
for  i in range(2,n//2):   #for  i in range(2,n): #for  i in range(2,n//4): 
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")

'''
import math as m
n=21
for  i in range(2,int(m.sqrt(16))):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")
