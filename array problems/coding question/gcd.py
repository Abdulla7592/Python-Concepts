'''def gcd(n1,n2):
    min=0
    if n1>n2:
        min=n2
    else:
        min=n1
    for i in range(1,min+1//2):
        if n1%i==0 and n2%i==0:
            g=i
    print(i)'''
def gcd(n1,n2):
    l=[]
    for i in range(1,min(n1,n2)):
        if n1%i==0 and n2%i==0:
            l.append(i)
    print(max(l))
    print(l)
n1=int(input())
n2=int(input())
gcd(n1,n2)
