def lpal(n1):
     n2=[]
     for i in range(len(n1)):
         sum=0# important mistake
         temp=n1[i]
         while temp!=0:
              rem=temp%10
              sum=sum*10+rem 
              temp=temp//10
         if sum==n1[i]:
            n2.append(n1[i])
     print(max(sorted(n2)))
     print(n2)
     print(n1)
              

n1=[1, 232, 5545455, 909090, 161]
lpal(n1)
