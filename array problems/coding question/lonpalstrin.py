def lpal(s1):
    l=[]
    t=0
    for i in range(len(s1)):
        t=s1[i]
        if t==t[::-1]:        
            l.append(t)
    l.sort()
    print(l)


        
    
    
s1=["apple","malayalam","ara","raar"]
lpal(s1)