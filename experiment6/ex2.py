d={}
n=int(input("enter number of key_value pair:-"))
for i in range(n):
    k=input("enter key:-")
    v=input("enter value:-")
    d[k]=v
rev={}
for k,v in d.items():
    rev[v]=k
    print("\n original dictionary:-")
    print(d)
    print("\n Reversed dictionary(values as keys):-")