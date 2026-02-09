a=60
b=70
c=80
d=75
e=90
sum=a+b+c+d+e
per=sum/5
print("Total mark is:-",sum)
print("percentage is :-",per)
if(per>=90 and per<=100):
    print("Grade is: O")
elif(per>=80 and per<90):
    print("Grade is:E")
elif(per>=70 and per<80):
    print("Grade is:A")
elif(per>=60 and per<70):
    print("Grade is:B")
elif(per>=50 and per<60):
    print("Grade is:C")
elif(per>=0 and per<50):
    print("Grade is:F")
else:
    print("Wrong input")

