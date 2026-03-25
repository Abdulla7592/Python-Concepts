s="geeks for geeks"
for i in s:
    print(i,end="")
for i in range(0,10,2):#with range 
    print(i)
for i in range(1,20,2):
    print(i)
l1=["apple","banana","oraange"]    
for index,element in enumerate(l1):#the enumerate function is used with for loop to iterate throigh the iterable while keep tracking of the index    
    print(index,element)     
for i in range(1,4):# nested for loop 
    for j in range(1,5):
        print(i,j)
l=[1,2,3,4,5]
for i in l:#for loop with list
    print(i)
numbers=[x for x in range(11)]# for loop in single line
print(numbers)
numbers=[i for i in l]
print(numbers)            
string=[x for x in s]
print(string)
# for loop with dictionary
d=dict()
d['xyz']=123
d['abc']=456
for i in d:
    print("%s %d" % (i, d[i]))
l2=["apple","orange"]    
for i in range(len(l2)):
    print("%d %s"%(i,l2[i]))
l3=[1,2,3,4,5]
for i in l3:#list elements are considered as i
    print("%d"%(i))    
for i in range(len(l3)):# cannot be used in dictionary because dictionary doesnot has integer index it has keyvalue
    print("%d %d"%(i,l3[i]))    
# we can use for i in d: because dictionary has both key or index and value   
d={"num":123,"age":23}
for i in d:
    print("{%s : %d}"%(i,d[i]))
#dictionary are not accessed with integer index it is acessed with key value which can be string or any type so d[i]doesnot provide integer index
t=(1,2,3,4,5)
for i in range(len(t)):
    print("%d %d"%(i,t[i]))
t=((1,2),(3,4),(5,6))   
for i,j in t:
    print(i,j)
for i in range(len(t)):
    print(i,t[i])
l=[[1,2],[3,4],[4,5]]  
for i in range(len(l)):
    print(i,l[i])  
for i ,j in l:
    print(i,j)
for i,j in t:
    print("(%d,%d)"%(i,j)) 
for i,j in l:
    print("[%d,%d]"%(i,j))
for i in t:
    print(i)    
l1=["apple","orange","banana"]
l2=["red","yellow","green"]
for i,j in zip(l1,l2):
    print(i, "is" ,j)
for i,j in enumerate(t):
    print(i,j)    
for i ,j in enumerate(l):
    print(i,j)    
    #continue statement 
    #continue statement return the control to the beginning of the loop
s="geeks for geeks"
k=[1,2,3,4,5]
k1=["apple","orange","banana"] 
t1=("apple","orange","banana")
t2=(1,2,3,4) 
for i in s:
    if i=="g":
        continue
    print(i)
for i in k:
    if i==4:
        continue
    print(i)
for i in k1:
    if i=="orange":
        continue
    print(i)
for i in t1:
    if i=="banana":
        continue
    print(i)
for i in t2:
    if i==3:
        continue
    print(i)    
#break statement in python
##break statement is used to bring control out of the loop
for i in s :
    if i=='r':
        break
    print(i)
for i in  k:
    if i==4:
        break 
    print(i)   
    #pass is used to write empty loops 
for i in s:#pass statement simply iterate and reach the limit and it has reache dthe last element so when we print an elemnet it print the last elemnt    
    pass
print(i)
a = 10
b = 20

# python ternary operator
min = "a is minimum" if a < b else "b is minimum"

print(min)