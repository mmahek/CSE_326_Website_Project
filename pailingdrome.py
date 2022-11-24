n=int(input("enter the number"))
b=0
while n>0:
    a=n%10
    b=b*10+a
    n=int(n/10)
print(b)
if int(b)==int(n):
    print("yes")
else:
    print("no")
    
