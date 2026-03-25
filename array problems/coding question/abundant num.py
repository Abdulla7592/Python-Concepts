def abund(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    if sum>n:
        return "abundant number"
    else:
        return "not"
n=int(input("enter the number:"))
print(abund(n))