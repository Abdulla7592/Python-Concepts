'''def fib(n):
    a=0
    b=1
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n==0:
        return -1
    else:
        for i in range(3,n+1):
            c=a+b
            a=b
            b=c
    return c   '''
def fib(n):
    a=0
    b=1
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n==0:
        return -1
    else:
        for n in range(3,n+1):
            c=a+b
            a=b
            b=c  
        return c

n=int(input("enter the number:"))
s=fib(n)
print(s)
if s==-1:
    print("error")


