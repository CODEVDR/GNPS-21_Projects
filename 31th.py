#Captcha
from random import *
i=0
while True:
    print(f"Captcha : {randint(1,9)}{chr(randint(97,122))}{chr(randint(97,122))}{randint(1,9)}{randint(1,9)}{chr(randint(97,122))}")
    i+=1
    if i==10:
        break