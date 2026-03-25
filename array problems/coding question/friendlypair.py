'''def friendly(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    if sum==n:
        return 1
    else:
        return 0'''
def friendly(n):
    sum=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if n//i==i:
                sum+=i
            else:
                sum=sum+i+n//i
    if sum==n:
        return 1
n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
if friendly(n1)==friendly(n2):
    print("friendly pair")
else:
    print("not friendly pair")