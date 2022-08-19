#18
#WAP IN PYTHON TO FIND POWER USING RECURSION FUNCTION:-
def pow(n,p):
   if p==0:
      return 1
   else:
      return n * pow(n , p-1)
#__main__
n=int(input("Enter A Number : "))
p=int(input("Enter The Power : "))
print(f"{n} power {p} is {pow(n,p)}")
