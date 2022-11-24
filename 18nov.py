'''#tuple


#1
t=(101,201,345,48)
b=min(tuple(t))
print("minimum of tuple t is",b)



#2
data=(input("Data:"))
t=data.split(",")
for i in range (len(t)):
    t[i]=int(t[i])
tup=tuple(t)
print("tuple:",tup)
print("sum:",sum(tup))



#3
data=(input("Data:"))
c=0
t=data.split(",")
tuple1=tuple(t)
print(tuple1)
element=input("element:")
if element in tuple1:
    c=tuple1.count(element)
    print("element exists ",c,"times.")
else:
    print("Invalid element")
    '''



#4
fruits={1: 'apple' , 2: 'orange' , 3: 'mango' , 4 : 'grapes'}
print(fruits.pop(4))
print(fruits)  # now value associated with key 4 has been deleted
print(fruits.popitem())
print(fruits)      # now value associated with key 3 has been deleted






















