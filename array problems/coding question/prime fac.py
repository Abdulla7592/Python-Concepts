def prime(n):
    flag=0
    if n<2:
        flag=1
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                flag=1
                break
    if flag==0:
        return n
def primefac(n):
    l=[]
    if prime(n)==n:
        l.append(n)
        return l
    else:
        for i in range(2,int(n//2)+1):
            if n%i==0:
                if prime(i)==i:
                    l.append(i)
    return l


n= int(input("enter the number:"))
print(primefac(n))