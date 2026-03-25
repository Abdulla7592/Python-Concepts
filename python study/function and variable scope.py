'''def fun(name):
    print("hello "+ name +" good")
    return name,"ahmad",28
name="abdulla"
print(fun(name))'''
'''a="abdulla ahmad n"
s="abd"
print(a)
print(a.upper())
print(a.lower())
print(a.isupper())
print(a.islower())
print(a.isalpha())
print(a.isalnum())
print(a.title())
print(a.startswith("a"))
print(a.startswith("abd"))
print(a.endswith("lla"))
print(a.replace("ahmad","aliya",5))
print(a.find("abdulla",0,12))
print(a.count("a",0,4))
s=a.swapcase()
print(s,a)
print(a.find("b"))
print(a.replace("b","d"))
s="pppppppppppppsssssssaaaaa"
s1=list(set(s))
print(len(s))
print(s.count("s"))
for i in range(len(s1)):
    count=0
    for j in range(len(s)):
         if s1[i]== s[j]:
            count+=1
            b=count
    print(b,s1[i])
print(sorted(s,key=s.count,reverse=True))
for i in range(len(s1)):
    for j in range(len(s)):
         if s1[i]== s[j]:
            b=s.count(s1[i])
    print(b,s1[i])'''
'''s="abdulla is a good boy"
print(s)
print(s[1:-1])
print(s[:6])
print(s[1:])
print(s[:-1])
print(s[-3:])
print(s[3::])
print(s[3:])
print(s[1::])
print(s[::1])
print(s[::-1])
s1="abdulla"
s2="aliya"
s3="Fathima"
s4="Nadarshaw"
s1+=" "+s2#concatenation take place and the string 1 is not changed and 2 is concatenated with it
print(s1)
s3=" ".join(s4)#here the s3 string is replaced with content of the s4 not actual concatenation
print(s3)
s4=" ".join(reversed(s3))#here the content of s3 is reversed and assigned to s4
print(s4)
l=[1,2,3,4,5]
s5=" ".join(str(l))
print(s5)
s6="geeks for geeks"
l=list(s6)
print(l)
print(s5)
c=" ".join(s6)#here the string s6 is assigned to c (also string)
print(c)
d=" ".join(l)#here the list of string is assigned to d
print(d)
print(s6)
s="123456"
d=list(s)
print(d)
s12=" ".join(d)
print(s12)
print(s12[4])
print(d[3])
for i,j in enumerate(s12):
    print(i,j)'''

l1=[1,2,3,4,5]
s="12345"
s1="geeks for geeks"
l2=list(s)#proper indexing is here
l3=list(s1)#proper indexing

