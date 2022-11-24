#the BMI calculator
weight=float(input("enter the weight in pounds"))
height=float(input("enter the height in inches"))
p=0.45359237
i=0.0254

w=weight*p
h=height*i
bmi=w/(h**2)
if bmi<18.5:
    print("underweight")
if 18.5<bmi<24:
    print("ideal")
