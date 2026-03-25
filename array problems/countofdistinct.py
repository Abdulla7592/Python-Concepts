l=[10, 20, 40, 30, 50, 20, 10, 20]
v=[]
v=l[0]
temp=0
print(len(l))
l1=list(set(l))
l1.sort()
print(l1)
for i in range(1,len(l)):
    temp=str(l[i])
    if temp not in v:
        v.append(int(temp))
print(v)
'''for i in range(len(l1)):
    count=0
    for j in range(len(l)):
        if l1[i]!=l[j]:
            count+=1
    print(count)'''