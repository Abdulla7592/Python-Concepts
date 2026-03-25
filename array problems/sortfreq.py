def freqsort(l):
    print(sorted(l,key=l.count,reverse=True))
l=[10, 20, 30, 40, 40, 50, 50, 50]
freqsort(l)