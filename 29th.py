from random import *
print("\t\t\t\tWELCOME TO CASINO GAME")
while True:
   lucky_no=randint(1,99)
   if int(input("Enter A Number : ")) ==lucky_no:
      print(f"computer choosen {lucky_no}")
      print("You Won")
   else:
      print(f"computer choosen {lucky_no}")
      print("You Loose")
   s=input("Do You Want Continue [Y/N]: ").upper()
   if s[0]=="N":
      break
      
