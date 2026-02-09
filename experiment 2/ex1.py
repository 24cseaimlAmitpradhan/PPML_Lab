p=float(input("enter pricipal amount:"))
t=float(input("enter time period in year:"))
r=float(input("enter rate of interst:"))
n=int(input("enter the number of times interst is compounded per year: :"))
si=(p*t*r)/100
print("simple interest=",si)
ci=(p*((1+(r/n))**(n*t)))
print("compund interet is:-",ci)
