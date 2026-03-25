#ternary operator
def adult(adult):
    adult=True if age>18 else False# example of ternary operator
    return adult
age=19
print(adult(age))
#string 
str1='abdulla'
str2=' is my name'
print(str1)
str1+= "" +str2
print(str1)
print(str1.lower())#convert to lower 
print(str1.upper())#convert to upper 
print(str1.islower())#check if it is lowercase
print(str1.isupper())#check if it is uppercase
print('abd'in str1)
r="abd\\\"ulla\""
s='abdu\lla'
print(r)
print(s)
print(str1[1:])
#bool
done=False
sone=False
check=True if done==True else False
print(check)
check=all([done,sone])
print(check)
check =any([done,sone])
print(check)
print(abs(-5.5))
print(round(5.6),round(5.57),round(5.47),round(5.546,2))
l1=["apple",'orange']
print("apple" in l1)
l2=[]
l2.append(l1)
print(l2)
l1[1]="passionfruit"
print(l1)
print(l1[::-1])
print(l1[:-1])
print(l1[0:-2])
print(len(l1))
l2.append('abdulla')
print(l2)
l2.extend(['abdulla',5])
print(l2)
l1+='dog'
l1+=['dog',5,'cat']
print(l1)
l1.remove('dog')
print(l1)
print(l1.pop())
print(l1)
l1.insert(2,'banana')
print(l1)
print(len(l1))
l1[4:9]=["Strawberry","blackberry","canberry","blueberry"]
print(l1)
print(len(l1))
l1.remove('d')
print(l1)
l1copy=l1[:]
l1.sort()
print(l1)
l1.sort()
print(l1)
print(l1copy)
print(sorted(l1))
l1=[1,2,5,4,0]
print(sorted(l1))# it returns the sorted list without chnaging the orginal list
print(l1)
l1.sort()#it permanently changes the orginal list 
print(l1)
print(l1.count(5))

