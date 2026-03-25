def prime(n1,n2):
    pr=[]
    for n in range(n1,n2+1):
        flag=0
        if n<2:
            continue
        elif n==2:
            pr.append(2)
            continue
        else:
            for x in range(2,int(n**0.5)+1):
                if n%x==0:
                    flag=1
                    break#breaks from the inside for loop
        if flag==0:
            pr.append(n)
    print(pr)



n1=int(input("enter the fisrt:"))
n2=int(input("enter the second:"))
prime(n1,n2)
