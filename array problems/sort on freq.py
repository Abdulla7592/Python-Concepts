def freqsort(l):
   l1=list(set(l))
   l1.sort()
   print(l1)
   for i in range(len(l1)):
      count=0
      for j in range(len(l)):
         if l1[i]==l[j]:
            count+=1
      print(l1[i],count)
   a=sorted(l,key=l.count,reverse=True)
   print(a)
l=[10, 20, 30, 40, 40, 50, 50, 50]
freqsort(l)

