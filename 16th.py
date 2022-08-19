#16
"""WAP IN PY TO DEF A FUNC THAT REPEATEDLY ASK THE USER TO ENTER PRODUCT NAME AND PRICES
STORE ALL OF THESE IN DICT WHOSE KEYS ARE THE PRODUCT NAME AND WHOSE VALUEDS ARE THE PRICES
WHEN THE USER IS DONE ENTERING PRO AND PRICES ALLOW THEM TO REP ENT A PRO NAME AND
PTR THE CORRESPONDING
PRICES"""
def store(p):
    while True:
       n=input("Enter A Product name: ")
       for i in p:
          if i==n:
             print(f"The Price of Entered Product is {p[i]}")
          else:
             print(f"ValueNotFound Error: Value Not Found, {n} is Not Found..")
       s=input("Do You Want To Search More[Y/N]: ")
       if s in "Nn":
            break

p={}
while True:
   n=input("Enter Product Name: ")
   n1=input("Enter Product Price: ")
   p[n]=n1
   s=input("Do You Want To Search More[Y/N]: ")
   if s in "Nn":
      break
store(p)
