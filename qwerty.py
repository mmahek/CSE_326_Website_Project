#armstrong number
'''num=int(input("n:"))
n=num
a=len(str(n))
s=0
b=" "
for i in range (0,a+1):
#while n!=0:
    b=n%10
    #print(b)
    s=s+b**3
    n=n//10
print(s)
if s==num:
    print("Armstrong number")
else:
    print("not an Artmstrong number")'''


num1=int(input("1:"))
num2=int(input("2:"))
#n=num
n=" "
for k in range (num1,num2+1):
    n=k
    a=len(str(k))
    s=0
    b=" "
    for i in range (0,a+1):
    #while n!=0:
        b=k%10
        #print(b)
        s=s+b**3
        k=k//10
    #print(s)
    if s==n:
        print("Armstrong number:",s)
    #else:
        print("not an Artmstrong number")


