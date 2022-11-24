#nested loops firsttime asked from ma'am
n=int(input("N:"))
for i in range(n,0,-1):
    for j in range(i):
       ''' print("*",end='')'''   #for printing the pattern including the asterick (*) symbol
       print(j+1,end='')          #for printing the pattern including numbers
    print()    
    
