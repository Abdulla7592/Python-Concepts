def perf(n):
    sum=0
    
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    if sum==n:
        print("perfect")
    else:
        print("not")
n=int(input("enter the number:"))
perf(n)