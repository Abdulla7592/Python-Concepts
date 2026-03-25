'''def arm(n):
    sum=0
    s=len(str(n))#integer cannot have len() func to calculate length of integer
    m=int(s)
    temp=n
    while(temp!=0):
        rem=temp%10
        sum=sum+rem**m
        temp//=10
    if sum==n:
        return 1
    else:
        return 0
n=int(input("enter the number:"))'''
'''arm(n)
if arm(n)==1:
    print("is armstrong")
else:
    print("not armstrong") '''
'''for n in range(1,n+1):
    if arm(n)==1:
        print(n)
    else:
        continue    '''
def arm(n):
    for n in range(1,n+1):
       sum=0
       temp=n
       s=len(str(n))
       m=int(s)
       while(temp!=0):
          rem=temp%10
          sum=sum+rem**m
          temp=temp//10
       if sum==n:
          print(n)
        
n=(int(input("enter the number:")))
arm(n)
'''for i in range(1,n+1):
    s=arm(i)
    if i==s:
        print(s)'''
   