'''n=int(input("enter the number:"))
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(a,",",b)
elif n==0:
    print("invalid Entry")
else:
    print("%d,%d"%(a,b),end="")
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
        print(",%d"%(c),end="")'''
n=int(input("enter the number:"))
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print("%d,%d"%(a,b))
elif n==0:
    print("invalid entry")
elif n>2:
    print("%d,%d"%(a,b),end="")
    for n in range(3,n+1):
        c=a+b
        a=b
        b=c
        print(",%d"%(c),end="")
       # print(c,end=",")
       


