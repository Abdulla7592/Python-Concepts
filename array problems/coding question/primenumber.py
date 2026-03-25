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
        return "prime"
    else:
        return "not prime"
n=int(input('enter the number:'))
s=prime(n)
print(s)
