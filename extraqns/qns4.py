# a=input("enter a string:")
# print(a[::-1])
# count=0
# for i in a:
#     if(i in ["a","i","o","u","e","A","I","O","U","E"]):
#         count+=1
# print("The vowel present in the string is:-",count)

 
st=input("enter a string:-")
rev=''.join(reversed(st))
print(rev)
vowel=0
consonant=0
for i in st:
    if i in 'aioueAIOUE':
        vowel=vowel+1
    else:
        consonant=consonant+1
print("The vowels are:",vowel)
print("The consonants are:",consonant)