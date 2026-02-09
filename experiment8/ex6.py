def rev(s):
    return (s if s=="" else(rev(s[1:])+s[0]))
n=input("entre a string:")
print(f"{n}reverse is:{rev(n)}")