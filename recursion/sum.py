def sum_digit(n):
    if n==0:
        return 0
    else:
        return n%10+sum_digit(n//10)
num=int(input("enter number:"))
print("sum of digits:",sum_digit(num))
