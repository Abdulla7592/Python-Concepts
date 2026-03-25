#is operator is used tocheck if 2 variables refers to same object
a=[1,2,3]
b=[1,2,3]
print(a is b)#false because it is refers to 2 diff object
c=a
print(a is c)
#== operator is used to check the content of 2 variable
print(a==b)
print(a==c)
#other case
x=10
y=10
print(x is y)#only for integer
z=[10]
print(x is z)
# in operator is used to check the presence of an elemnt in object 
#2 uses are there for in operator #
#1 used to check element present in  list tuple range string etc
# 2 used to iterate through a sequence in a for loop
l=[1,2,3,4,5]
if 5 in l:
    print("found")
for i in l:
    if i==4:
        break
    print(i)

print ("braeked") 
l1=range(5)
for i in l1:
     print(i)
if 3 in l1:
       print("found")