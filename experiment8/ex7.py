def vowelcount(s):
    count=0
    for i in s:
        if i in['a','i','o','e','u','A','E','I','o','U']:
            count+=1
    return count
n=input("enter a string:")
print(f"{n}contains{vowelcount(n)}vowels.")