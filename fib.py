def fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)
n=int(input("enter the value:"))
print("The value of",n,"fibonaaci number will be",fib(n))   
    
