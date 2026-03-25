"""def sec(l):
    temp=0
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            temp=l[i]
            l[i]=l[i+1]
            l[i+1]=temp 
    print(l[len(l)-2])
l=[1,2,3,6,4,8]
sec(l)"""
l=[1,2,3,6,4,8]
s=sorted(l)
print(s[-2])
