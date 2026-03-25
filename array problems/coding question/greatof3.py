n1=20
n2=30
n3=50
if n1>n2:
    if n1>n3:
        print("first number is greater")
elif n2>n3:
    if n2>n1:
        print("second number is greater")
else:
    print("third number is greater")          
    #using ternary operator
n1,n2,n3=30,40,50 
max=n1 if n1>n2 else n2
max=n3 if n3>max else max 
print(max)        