def gcd(a,b):
   if b==0:
      return a
   else:
      return gcd(b,a%b)
n=int(input("Enter First Number : "))
n1=int(input("Enter Second Number : "))
print(f"GCD of {n} and {n1} is : {gcd(n,n1)}")
