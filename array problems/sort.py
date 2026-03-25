a=[23,54,12,10,15]
a.sort()
print(a)
print(a[::-1])
a.sort(reverse=True)
print(a)
a=[23,54,12,10,15]
n=len(a)
l1=[]
for i in range(0,n-1):#bubble sort
    for j in range(i+1,n):
        if a[i]>a[j]:
            temp=a[j]
            a[j]=a[i]
            a[i]=temp
print(a)
