f=open("poem.txt")
c=f.read()
st,dg,sp=0,0,0
for i in c:
   if i.isalpha():
      st+=1
   elif i.isdigit():
      dg+=1
   else:
      sp+=1
print(f"Number of Alphabets Count is {st}.\nNumber of Digit Count is {dg}.\nSpecial Character Count is {sp}.")
