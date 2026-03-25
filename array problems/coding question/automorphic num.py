def auto(n):
    sq=pow(n,2)
    mod=pow(10,len(str(n)))
    if sq%mod==n:
        return "automorphic"
    else:
        return "not automorphic"
def autos(n):
    s=n*n
    a=str(s)
    b=str(n)
    if a.endswith(b):
        return "automorphic"
    else:
        return "not automorphic"
    


n=int(input("enter the nmber:"))
print(auto(n))
print(autos(n))