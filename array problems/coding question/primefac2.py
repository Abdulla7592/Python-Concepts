def primefac(n):
    l=[]
    d=2
    while n>1:
        if n%d==0:
            l.append(d)
            n=n//d
        else:
            d=d+1
    return list(set(l))


    







n=int(input("enter the number:"))
print(primefac(n))