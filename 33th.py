f=open("lines.txt",newline="")
c=f.read()
c=c.split("\n")
ct=0
for i in c:
   try:
      if i[0] in "Aa":
         ct+=1
   except IndexError as err:
      print(err)
print(f"The No of lines starting with character 'a' is {ct}")
