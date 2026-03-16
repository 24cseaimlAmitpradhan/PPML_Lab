#wap to crete an integer list of 20 elements increase the odd valued element by 5
s=[]
x=int(input("enter the number of elements:"))
for i in range(x):
    n=int(input("enter the elements:"))
    s.append(n)
for i in range(x):
    if s[i]%2!=0:
        s[i]=s[i]+5
print(s)
