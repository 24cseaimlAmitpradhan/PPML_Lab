def si(p,r,t):
    return (p*t*r)/100
p=float(input("enter principal amount:"))
r=float(input("enter rate of interst:"))
t=float(input("enter time period in year:"))
print("simple interst is:",si(p,r,t))