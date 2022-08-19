#WAP IN PYTHON TO DEFINE A FUNC THAT WILL ACCEPT
#A STRING AS PARAMETER AND RETUEN NUMBER OF VOWELS
def vowels(n):
   n=n.lower()
   c=0
   for i in n:
      if i=="a" or i=="e" or i=="o" or i=="i" or i=="u":
         c+=1
   return c

v=vowels(input("Enter A String: "))
print(v)
