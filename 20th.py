#20
#WAF IN PYTHON TO DISPALY FIBONACCI SERIES USING RECURSION:-
def fibo(n):
   if n==0:
      return 0
   if n==1:
      return 1
   else:
      return fibo(n-1) + fibo(n-2)
n=int(input("Enter A Number : "))
for i in range(n):
   print(fibo(i))
print(f"The Sum Of Fibonacci Series is : {fibo(n)}")
