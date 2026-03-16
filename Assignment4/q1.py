#wap to print second largest and second smallest element in a list of 10 integers without using sort function
arr=[]
x=int(input("enter the number of elements:"))
for i in range(x):
    m=int(input("enter the elements:"))
    arr.append(m)
for j in range(len(arr)-1):
    for k in range(len(arr)-j-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
print("The sorted array is:")
print(arr)
second_largest=arr[-2]
second_smallest=arr[1]
print("The second largest elements is :",second_largest)
print("The second smallest elements is :",second_smallest)