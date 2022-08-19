#4
def armstrong_no(n):
   s=0
   for i in n:
      s+=int(i)**3
   if s==int(n):
      return f"{n} is a Armstrong Number"
   else:
      return f"{n} is Not A Armstrong"

v=armstrong_no(input("Enter A Value to Check Weather The Number is Armstrong or Not: \n")) 
print(v)
