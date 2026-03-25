a=[23,54,12,10,43]
print(a[::-1])
n=len(a)
temp=0
for i in range(n//2):
    temp=a[i]
    a[i]=a[n-i-1]
    a[n-i-1]=temp
print(a)