#15
"""WAP IN PYTHON TO DEFINE A FUNC THAT INPUT
ELEMENTS IN TUPLE AND PASS IT TO FUNC TO DETERMINE
TOTAL NUMBER OF EVE AND ODD NUMBERS IN IT"""
def eve_odd(n):
   e,o=0,0
   for i in n:
      if i%2==0:
         e+=1
      else:
         o+=1
   return e,o

t=()
t=eve_odd(eval(input("Enter A Tuple: ")))
print(f"Even Number Count is: {t[0]} \nOdd Number Count Is {t[1]}")
#print("Even Number Count is:",t[0],"\n","Odd Number Count Is: ",t[1]})
