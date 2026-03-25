def strong(n):
    temp=n
    sum=0
    while(temp!=0):
        r=temp%10
        f=1
        i=1
        while(i<=r):
            f=f*i
            i=i+1
        sum=sum+f
        temp=temp//10
    if sum==n:
        print("strong")
n=145
strong(n)