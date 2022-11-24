#printing the even values from 50 to 100
'''def even():
    for i in range (a,b):
        if i%2==0:
            print(i)
        
a=int(input("enter the starting of range"))
b=int(input("enter the end"))
even()'''
def ev():
    for i in range (50,101):
        if i%2==0:
            return i
r=101
while r:
    print(ev())
    r=r-1
