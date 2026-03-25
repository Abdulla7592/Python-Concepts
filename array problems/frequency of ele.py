def freq1(a):# second concept
    n=len(a)
    l=[]
    l.append(a[0])
    for i in range(1,n):
        if a[i] not in l:
            l.append(a[i])
    l.sort()
    print(l)
    for i in range(len(l)):
        count=0
        for j in range(len(a)):
            if l[i]==a[j]:
                count+=1
        print(l[i],count)
def freq(a):# first concept
    n=len(a)
    b=list(set(a))
    print(b)
    for i in range(len(b)):
        count=0
        for j in range(n):
            if b[i]==a[j]:
                count+=1
        print(b[i],count)
a=[10, 30, 10, 20, 10, 20, 30, 10]
freq(a)
freq1(a)
