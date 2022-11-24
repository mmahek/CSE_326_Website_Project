#area of circle but if radius is negative then return nothing
def area(radius,pi=3.141):
    if radius<0:
        return 
    else:
        return pi*radius*radius
radius=float(input("Enter the value of radius"))
#calling of function while printing the area.
print("The area of circle is", area(radius))        
