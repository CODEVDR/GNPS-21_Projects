f=open("poem.txt")
c=f.read().lower()
ct=0
for i in c:
   if i in "aeiou":
      ct+=1
print(f"Count Of Vowels are {ct}")
