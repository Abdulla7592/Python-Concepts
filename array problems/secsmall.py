a=[23,54,12,10,15]
a.sort()
print(a[1])
a=[23,54,12,10,15]
b=sorted(a)
print(b[1])
a=[23,54,12,10,15]
f=100
for i in range(len(a)):
    if a[i]<f:
        f=a[i]
sec=1001
for i in range(len(a)):
    if a[i]!=f and a[i]<sec:
        sec=a[i]
print(sec)
a=[23,54,12,10,15]
min=a[0]
for i in range(1,len(a)):
    if min>a[i]:
        min=a[i]
m=100
for i in range(len(a)):
    if a[i]!=min and m>a[i]:
        m=a[i]
print(m)
        