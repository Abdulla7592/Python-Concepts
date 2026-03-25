n=int(input("enter the year:"))
if n%400==0:
    print("it is leap year")
if n%4==0 and n%100!=0:
    print("the year is leap year")
else:
    print("not leap")        