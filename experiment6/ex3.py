i=input("enter a sentence:-")
List1=i.split()
print("\n elements of list1 with index:-")
for i,w in enumerate(List1):
    print(i,w)
List2=list(range(1,len(List1)+1))
List3=list(zip(List1,List2))
print("\n customize list using zip:-")
print(List3)