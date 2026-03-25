a=[23]
a=[23,54,12,10,15]
n=len(a)
a.sort()
for i in range(n//2):
    print(a[i],end=",")
for i in range(n-1,n//2-1,-1):
    print(a[i],end=",")
    print(end="")