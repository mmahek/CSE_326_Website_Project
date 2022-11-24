#return multiple values by keyword return
def demo(r):
    return 3.1412*r*r , 2*3.1412*r
r=float(input("Enter the value for radius:"))
area,circumference=demo(r)
print("The area of circle with radius=",r,"is area=",area)
print("The circumference of of circle with radius=",r,"is circumference=",circumference)       
