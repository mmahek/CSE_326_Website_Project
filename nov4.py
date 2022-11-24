#center
'''a="python"
print(a.center(10,'@'))
#swapcase
print(a.swapcase())
#split
b="this is title"
print(b.split())
print(b.swapcase())
print(b.center(20,'$'))
print(a.center(11,'#'))

s=input("Enter the String: ")
b='@'
l=len(s)
#print(l)
print(s.upper())
print(s.title())
print(s.split())
print(s.center(l+int(input("Enter the number of spaces: ")),input('Enter the desired character to be filled: ')))
print(s.lower())
print(b.join(s))
print(s.replace(input("Enter the Word to Be replaced: "),input("Enter the word that will Replace: ")))'''


#more functions
'''s1='Book'
s2='School'
print(s1*3+s2)

a=input("Enter the 1st String plz.: ")
b=input("Enter the 2nd string : ")
c=input("Enter the 3rd string: ")
print("is upper:",a.isupper())
print("is lower:",a.islower())
print("is digit:",b.isdigit())
print(":",a.istitle())
print(c.isspace())
print(a.isalpha(),b.isalpha(),c.isalpha())
print(b.isalnum(),c.isalnum())

#3
s="Python provides built - in libraries \n Using Python we can implement more and more applications \n\t Python is Robust"
print(s)


#4


s1=input()
s2=input()
l1=len(s1)
l2=len(s2)
if l1==l2:
    print("strings have same length")
elif l1>l2:
    print(s2+s1+s2)
elif l1<l2:
    print(s1+s2+s1)'''
#5

s=input("Enter the string: ")
if (s.startswith('Python'))==True and (s.endswith('Programming'))==True :
    print("valid")
print("character with min val: ", min(s))    






