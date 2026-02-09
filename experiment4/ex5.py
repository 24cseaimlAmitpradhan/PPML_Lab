n=343
rev=0
while(n>0):
    temp=n%10
    n=n/10
    rev=rev*10+temp
if(n==rev):
    print("The number is palindrome")
else:
    print("The given number is not a palindrome ")