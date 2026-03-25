# using while loop
def fact2(n):
    i=1
    while(i<n):
        if n%i==0 and i!=1:
            print(i)
        i=i+1
        
# usinf for loop
def fact1(n):
    for i in range(1,n+1):
        if n%i == 0:
            print(i)
        else:
            continue    
n=int(input("enter the number:"))
fact2(n)  
fact1(n)      