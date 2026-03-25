'''n=int (input("enter the number"))
sum=0
for i in range(n+1):
    sum+=i
print(sum)
sum1=n*(n+1)//2
print(sum1)'''
#sum of numbers from a range
n1,n2=2,5
sum=0
for i in range(n1,n2+1):
    sum+=i
print(sum)
sum=n2*(n2+1)//2-n1*(n1+1)//2+n1
print(sum)