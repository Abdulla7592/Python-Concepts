'''def freq(n):
    l1=[]
    s=len(n)
    print(s)
    for i in range (s):
        l1=list(n)
        l2=list(set(n))
    print(l2)
    for i in range(len(l2)):
        count=0
        for j in range(s):
            if l2[i]==n[j]:
               count+=1
            
               
        print(l2[i],count)'''
def freq1(n):
    l=[]
    l.append(n[0])
    for i in range(1,len(n)):
        if n[i] not in l:
            l.append(n[i])
    for i in range(len(l)):
        count=0
        for j in range(len(n)):
            if l[i]==n[j]:
                count+=1
        print(l[i],count,end=",")        
n="elephant"
#freq2(n)
freq1(n)
