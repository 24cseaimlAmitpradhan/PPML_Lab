a=int(input("enter a:-"))
b=int(input("enter b:-"))
c=int(input("enter c:-"))
d=b*b-4*a*c
if(d>0):
  p1=(-b+math.sqrt(d))/(2*a)
  p2=(-b-math.sqrt(d))/(2*a)
  print("Two real root:",p1,p2)
elif(d==0):
    p=-b/(2*a)
    print("The real root:",p)
else:
    print("No real roots.")
