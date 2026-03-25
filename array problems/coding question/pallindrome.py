'''n=int(input("enter the number:"))
sum=0
temp=n
while(temp!=0):
    rem=temp%10
    sum=sum*10+rem
    temp=temp//10
print(sum)    
if (sum==n):
    print("pallindrome")
else:
    print("not pallindrome")    '''

# pallindrome number upto a range
def pal(n):
   sum=0
   temp=n
   while(temp!=0):
       rem=temp%10
       sum=sum*10+rem
       temp=temp//10  
   if (sum==n):
     return 1
   else:
     return 0


for n in range(1,122):
   pal(n)
   if pal(n)==1:
      print(n)
   else:
      continue   

   