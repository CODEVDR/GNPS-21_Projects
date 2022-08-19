f=open("poems.txt",newline="")
c=f.read().upper()
c=c.split()
ct=0
ct1=0
for i in c:
   if i=="TO":
      ct+=1
   elif i=="THE":
      ct1+=1
print(f"Total 'to' Count is : {ct}\nTotal 'the' Count is : {ct1}")
      
