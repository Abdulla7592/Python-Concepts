x=10 #donot need any command for declaring variable it is declared the moment a value is added
y="abdulla"#assigned to it
z='aliya'#can also use single quotes 
s="""aliya"""#can also use triple quotes 
print(s)
print(x,y,z)#can print multiple variable using comma operator
x,y,z=10,'abdulla',3j#can assign value to multiple variable in a single line using commas
print(x,y,z)
x=10
y="abdulla"
x=20.5#once the varible value is given it can be changed in the next line it is not fixed
print(x,y)
#type casting we can specify the datatype of the variable
x=int(3)
y=float(20.4)
z=complex(3j)
# using the type() func we can output the datatype of the given variable
print(type(x))
print(type(y))
print(type(z))
#case sensitivity 
a=0
A=4
print(a,A)
#givingsingle value to multiple variable
x=y=z="orange"
print(x,y,z)
#unpacking a collection 
fruit=["apple","oranges","banana"]
x,y,z=fruit
print(x,y,z)#the values inside fruit collection is assigned to the variables x,y,z
print(fruit)#entire thing after = is displayed 
#printing multiple string value using + operator
str='abdulla '
str2="ahmad "
str3="""n """
print(str+str2+str3)
#incase of integer the values are added or addition take place
print(a+A)
#if we try to print 2 different datatype inside a print function using +operator error occurs
print(A,x)#comma operator is used to print two different datatypes
#global variable defined outside function and can be accessed both inside and outside function 
"""x= 'fantastic '
def myFunc():
        print("the value of x:",x)
myFunc()"""
#local variables are declared inside  the function and accessed within the function and the same 
# local and global variable will not affect both they are independent 
"""x='brilliant'#global variable
def myFun():
    x="fantastic"#local variable
    print("the value is:",x)
print("the value of global:",x)
myFun()""" 
#global keyword used to access global variable inside a local function
#also can change the value of global variable inside local fun()
x='FANTASTIC'
def myFun():
    global x
    x="brilliant"
    print("the value of x is :",x)
myFun()
print(x)#same x is printed because global variable so changed
y="nanda"
def myfun():
    print(y)
myfun()    
#the global keyword is used when we want to change a global variable 
# inside a local function


