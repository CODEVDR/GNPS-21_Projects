#22.	WAP in python to define a user-defined function that accepts a string and calculates the number of upper case letters and lower case letters.
def ck(str):
   up,lw=0,0
   for i in str:
      if i.isupper():
         up+=1
      elif i.islower():
         lw+=1
   return(up,lw)

s="GnPs21"
k=ck(s)
print(f"The number of lowercase count is {k[1]}\nThe number of uppercase count is {k[0]}")
