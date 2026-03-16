#wap to create two list . first list containing 5 integers and second list containing 5 string. print both the list one lements from each list combined at a time
list1=[1,2,3,4,5]
list2=["A","B","C","D","E"]
x=[]
for i in range(len(list1)):
    x.append(str(list1[i]))
    x.append(list2[i])
print(x)