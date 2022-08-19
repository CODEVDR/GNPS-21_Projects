print("Implemetation of Stack")
stack=[]
top=-1
def push(st,val):
   st.append(val)
   top=len(st)-1
def pop(st):
   if stack==[]:
      print("stack is underflow")
   else:
      res=st.pop()
      top=len(st)-1
      return res
def peek(st):
   top=len(st)-1
   print(f"Top is printed to {st[top]}")
def disp(st):
   top=len(st)-1
   print(f"{st[top]} <==TOPMOST ELEMENT")
   for i in range(len(st)-1):
      print(st[top-1])
      top-=1
ch='y'
while ch in "Yy":
   print("1.Push")
   print("2.Pop")
   print("3.Peek")
   print("4.disp")
   print("5.Exit")
   n=int(input("Enter Your Choice : "))
   if n==1:
      val=int(input("Enter A Value : "))
      push(stack,val)
      print(f"Updated Stack {stack}")
   elif n==2:
      k=pop(stack)
      print(f"Popped Item : {k}\nUpdated Stack : {stack}")
   elif n==3:
      peek(stack)
   elif n==4:
      disp(stack)
   elif n==5:
      print("Exiting..")
      break
