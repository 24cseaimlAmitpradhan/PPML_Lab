def largest(a,b,c):
    return a if(a>b and a>=c)else b if(b>=c)else c
a=int(input("enter frist number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
print("Largest among these three numbers is:",largest(a,b,c))