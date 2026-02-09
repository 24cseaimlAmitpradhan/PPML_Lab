l=["apple","banana","mango"]
print("fruit display from last index to first index with their lengths:-")
for i in l[::-1]:
    print(i,"-length:",len(i))
    print("\n list containing reverse of each fruit name,")
    rev=[]
    for fruit in l:
        rev.append(fruit[::-1])
        print(rev)