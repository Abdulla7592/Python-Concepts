a=[10,12,5,6,98,11]
print(max(a))
a.sort()
print(a[-1])
'''max=a[0]
for i in range(1,len(a)):
    if max<a[i]:
        max=a[i]
print(max)'''
a=[10,12,5,6,98,11]
temp=0
n=len(a)
for i in range(0,n):
    for j in range(i+1,n):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)
print(a[0])
