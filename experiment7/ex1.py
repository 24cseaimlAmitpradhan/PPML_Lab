m=int(input("entre starting of the natural number:"))
n=int(input("entre ending of the natural number:"))
l=[x for x in range(m,n+1)]
print("The sum of the list is:-",sum(l))
print("The avarage of the list is:-",(sum(l)/len(l)))
print("The largest element in the list is:-",max(l))
print("The smallest element in the list is:-",min(l))
l2=[x for x in l if x%3!=0]
print("The element which are not divisible by 3 are:-",l2)