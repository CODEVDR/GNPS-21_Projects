#WAP IN PYTHON TO DEFINE A USER DEF FUNC THAT
#ACCEPTS A STRING AND COUNT THE NUMBER OF UPPER
#CASE AND lOWERCASE
def case(n):
   up=0
   lw=0
   for i in n:
      if i in n.upper():
         up+=1
      else:
         lw+=1
   return up,lw

t=case(input("Enter A String: "))
print(f"Uppercase Letter Count is {t[0]} \nLowercase Letter Count is {t[1]}")
         
