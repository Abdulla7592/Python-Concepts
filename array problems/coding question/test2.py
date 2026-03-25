def fracadd(f1,f2):
    n1,d1=map(int,f1.split("/"))
    n2,d2=map(int,f2.split("/"))
    res_num=(n1*d2)+(n2*d1)
    res_deno=d1*d2
    def gcd(res_num,res_deno):
        for i in range(1,min(res_num,res_deno)):
            if res_num%i==0 and res_deno%i==0:
                gcd=i
        return gcd
    com_div=gcd(res_num,res_deno)
    a=res_num//com_div
    b=res_deno//com_div
    print("%d/%d"%(a,b))

f1=input("enter the first fraction")
f2=input("enter the second fraction")
fracadd(f1,f2)
