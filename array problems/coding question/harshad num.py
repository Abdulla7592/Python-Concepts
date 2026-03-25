def harsh(n):
    temp=n
    sum=0
    while temp!=0:
        r=temp%10
        sum=sum+r
        temp=temp//10
    if n%sum==0:
        return "harshad number"
    else:
        return "not harshad"
n=int(input("enter the number:"))
print(harsh(n))