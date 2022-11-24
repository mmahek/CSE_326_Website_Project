#1.Addition
#2.Subtraction
#3.Multiplication    
#4.Division
#5.Mod 
#6.SquareRoot    
#7.Exponent
#8.Sine
#9.Cosine
#10.Tangent
#11.Degree to Radians
#12.Radians to Degrees
#13.Factorial

import math

sub=0
add=0
mul=1
#1.Addition
ch=0
while ch !=14:
    print("\n")
    print("\n")
    print("***************************************SCIENTIFIC CALCULATOR****************************************")
    print("1.Addition","2.Subtraction","3.Multiplication","4.Division","5.Mod","6.SquareRoot","7.Exponent","8.Sine","9.Cosine","10.Tangent","11.Degree to Radians","12.Radians to Degrees","13.Factorial", "14.Exit",sep="\n\n")
    try :
        print("\n")
        ch=int(input("Enter the ch Number to be performed: "))
    except:
        pass
    if ch==1:
            n=int(input("Enter the number of values to be entered for addition : "))
            for i in range(0,n):
                n1=float(input("Enter the number: "))
                add=add+n1
            print("The addition of ",n,"digits is",'%.2f'%add)


    #2.Subtraction
    elif ch==2:


    #3.Multiplication    
     elif ch==3:
            n=int(input("Enter the number of values to be entered for multiplication : "))
            for i in range(0,n):
                n1=float(input("Enter the number: "))
                mul=mul*n1
            print("The multiplication of ",n,"digits is",'%.2f'%mul)



    #4.Division
    elif ch==4:     
                n1=float(input("Enter the dividend: "))
                n2=float(input("Enter the divisor: "))
                div=n1/n2
                print("The quotient of division is",'%.2f'%div)



    #5.Mod 
    elif ch==5:
                n1=float(input("Enter the dividend: "))
                n2=float(input("Enter the divisor: "))
                modv=n1%n2
                print("The mod value  is",'%.0f'%modv)


    #6.SquareRoot    
    elif ch==6:
            n1=float(input("Enter the number"))
            sqrt=math.sqrt(n1)
            print('%.2f'%sqrt)



    #7.Exponent
    elif ch==7:
                n1=float(input("Enter the base: "))
                n2=float(input("Enter the exponent:"))
                exp=math.pow(n1,n2)
                print("The exponent of  base",n1,"and power",n2,"is",exp)




    #8.Sine
    elif ch==8:
        rad=int(input("Enter the radians: "))
        s=math.sin(rad)
        print("The Sine of",rad,"is",s)



    #9.Cosine
    elif ch==9:
        rad=int(input("Enter the radians: "))
        c=math.cos(rad)
        print("The Cosine of",rad,"is",c)



    #10.Tangent
    elif ch==10:
        rad=int(input("Enter the radians: "))
        t=math.tan(rad)
        print("The Tangent of",rad,"is",t)



    #11.Degree to Radians
    elif ch==11:
            deg=int(input("Enter the degrees to convert into radians: "))
            rad=math.degrees(deg)
            print("The value of",deg,"degrees in radians is",'%.2f'%rad)




    #12.Radians to Degrees        
    elif ch==12:
            rad=int(input("Enter the radians to convert into degrees: "))
            deg=math.radians(rad)
            print("The value of",rad,"radians in degree is",'%.2f'%deg)




    #13.Factorial
    elif ch==13:
        n=int(input("Enter the Number: "))
        fact=(math.factorial(n))
        print("The factorial of",n,"is",fact)

    elif ch==14:
            print("thankyou for using our calculator")
    else:
        print("please enter a number btw 1 to 14 only ")
        a=input("press enter ")




