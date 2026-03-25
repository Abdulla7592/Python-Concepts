#method 1
'''n=int(input("enter the number:"))
if n>0:
    print("is positive")
elif n==0:
    print("is zero")
else:
    print("is negative")'''

#ternary operator
n=int(input("enter the number:"))
print("positive") if n>0 else print("negative")