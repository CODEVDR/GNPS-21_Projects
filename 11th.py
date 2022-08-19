#11
#WAP IN PYTHON TO PERFORM AIRITHMATIC CALCULATION AND RETURN MULTIPLE RESULT
#USING TUPLE VARIABLE
def multi_var_tup(a,b):
   m=a*b
   d=a/b
   return m,d
v=multi_var_tup(10,20)
print(f"Multiplication is {v[0]} and Division is {v[1]}")
