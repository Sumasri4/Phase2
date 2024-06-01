l=[8,3,5,6,7,2]
for i in range(1,len(l)):
    m=l[i]
    j=i-1
    while j>-1 and m<l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=m
print(l)
