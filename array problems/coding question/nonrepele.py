def nrep(n):
    l=[]
    for i in range(len(n)):
        l.append(n[i])
        l1=list(set(l))
    print(list(set(l)))   
    print(l)
    for i in range(len(l1)):
        count=0
        for j in range(len(n)):
            if l1[i]==n[j]:
                count+=1
        if count==1:
            print(l1[i])
    else :
        print("no element")
n="geeks for geeks"
nrep(n)