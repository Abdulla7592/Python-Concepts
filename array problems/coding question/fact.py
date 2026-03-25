n=int(input("enter the number:"))
f=1
i=1
t=f
while(i<=n):#using while loop requires variable iteratio separate
    f=f*i
    i=i+1
print(f) 
for i in range(1,n+1):# using for loop
    t=t*i
print(t)
