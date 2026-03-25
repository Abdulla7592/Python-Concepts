d={"name":"abdulla","age":"24","color":"green"}
print(d)
print(d["name"])#acessing the key value usinkey
print(d["age"])
print(len(d))
for i in d:#looping through dict
    print(i,d[i])
    print("{%s:%s}"%(i,d[i]))
print(d.items())#printing all items in the list 
print(d.keys()) #printing th key value
print(d.get("name"))#getting the corresponding value of key
print(d.get("color"))
print(d.get("age"))
print(d.get("fruit","apple"))#geting the value of fruit key if not present then defauit valur is printed 
print(d.get("fruit"))# print none
print(d)
d["fruit"]="apple"#giving new key and value at the end of the dict
print(d)
print(d.pop("name"))#deleting the value and key
print(d)
print(d.popitem())# deleting the last entered key and value
print(d)
print(d.setdefault("fruit","apple"))
print(d)
print(d.setdefault("name","abdulla"))
print(d)
print(d.items())
print(list(d.items()))
print(tuple(d.items()))
d1={}
d1.update(d)
print(d1)
d["123"]=12
print(d)