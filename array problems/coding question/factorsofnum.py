def fac(n):
   i=1
   while(i<=n):
      if n%i==0:
         print("%d,"%(i),end="")
         print(end="")
      i=i+1
   '''for i in range(1,n+1):
      if n%i==0:
         print(i,end=" ")'''
   '''' l=[]
    for x in range(1,n+1):
        if n%x==0:
            l.append(x)
    return l'''
            
















n=int(input("enter the number:"))
fac(n)
#print(fac(n))
