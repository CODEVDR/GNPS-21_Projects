#find sum of first ‘n’ natural number
def sum(n):
   if n==1:
      return 1
   else:
      return n + sum(n-1)
#__main__
print(sum(int(input("Enter A Number : "))))
