number=13
devisor=2
factor=[]
while number>1:
    print(number)
    if number%devisor==0:
        factor.append(devisor)
        number=number//devisor
    else:
        devisor+=1
    
    
a=list(set((factor)))
print(a)