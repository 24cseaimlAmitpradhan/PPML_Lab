a=14;count=0;i=1
while(i<=a):
    if(a%i==0):
        print("The number is :",a)
        count+=1
        i+=1
    if(count==2):
        print("The given number is a prime no.")
    else:
        print("The given number is not a prime no.")