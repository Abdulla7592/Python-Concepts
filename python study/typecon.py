s="10010"
f=12.3
str='a'
a=45
print(int(s,2))#converting a string of base 2 to integer 
print(int(f))#converting float value to integer
print(float(s))#converting to float value
print(ord(str))#converting a character to its corresponding ascii number
print(hex(a))#converting to hexadecimal number from integer
print(oct(a))#converting integer to octadecimal 
str1='ABDULLA'
print(tuple(str1))
print(list(str1))
print(set(str1))
print(complex(a,2))#converting to complex number with real and imaginery
n="12345"#int is not iterable so it cannot be converted into list or tuple
print(list(n))