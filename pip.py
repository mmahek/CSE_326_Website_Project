#simple interest
def simple_in(p,t,r=8):
    n=p*r*t/100
    print("The simple interest for given values of p=",p,"t=",t,"and r=",r,"is=",n)
p=float(input("enter the principle amount"))
t=int(input("enter the time in years"))        
simple_in(p,t)    
