n=int(input("enter a number:-"))
if(n<0):
    print("factorial of the number not defined")
else:
    fact=1
    i=1
    while i<=n:
        fact*=i
        i+=1
        print("factorial is:-",fact)