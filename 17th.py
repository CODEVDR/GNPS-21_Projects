#17
#WAP IN PYTHON TO FIND FACTORIAL OF A NUMBER USING RECURSION
def fact(n):
   if n==1:
      return 1
   else:
      return n*fact(n-1)
#__main__
n=int(input("Enter A Number : "))
print(f"Factorial Of Entered Number {n} is:- \n{fact(n)}")
