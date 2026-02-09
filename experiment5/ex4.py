l=[]
n=int(input("enter the number of terms to be entered:-"))
for i in range(n):
    l.append(int(input(f"enter{i+1}th number:-")))
    res=sorted(list(set(l)))
    print("after removing the duplicate elements and sorting the list:-",res)