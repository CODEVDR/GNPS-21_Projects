#WAP IN PYTHON TO DEFINE A FUNCTION THAT WILL ACCEPT
#STRING AS PARAMETER  ,COUNT THE NO. OF TIMES THE
#THE ENTER CHARACTER PRESENT INSIDE IT.
def char(n,n1):
   n=n.lower()
   n1=n1.lower()
   c=0
   for i in n1:
      if i==n:
         c+=1
   return c

n1=input("Enter a String: ")
n=input("Enter a character That You Want to Search in above string: ")
v=char(n,n1)
print(v)
