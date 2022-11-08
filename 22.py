'''name=input()
y=input()
b=(name[0:3]+"@"+y)
print(b)'''

num=int(input())
sum=0
while num!=0:
    digit=int(num%10)
    sum += digit
    num=num/10
print(sum)    
