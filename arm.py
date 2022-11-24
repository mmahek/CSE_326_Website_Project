#armsrrong number
n=int(input("enter the number:"))
sum=0
while n>0:
    a=n%10
    x=a**3
    n=int(n/10)
    sum=sum+x
print(sum)    
if n==sum:
    print("the given input",n,"is a armstrong number.")
else:
    print("the given number is not an armstrong number")
