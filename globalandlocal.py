#global keyword
'''a=19
def dem():
    global a
    a=91
    print("the value of local a is",a)
print(a)
dem()
print(a)
'''
#local keyword
b=29
c=23
def med():
    c=98
    global c
    print("the value of local variable is",b,c)
print(b,c)
med()
print(b,c)
