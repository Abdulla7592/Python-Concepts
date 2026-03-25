def power(n,r):
   '''n=pow(n,r)
   return n'''
   '''' sum=1
    for x in range(1,r+1):
        sum*=n
    return sum'''
   n=n**r
   return n
    








n=int(input("enter the number:"))
r=int(input('enter the number'))
power(n,r)
print(power(n,r))