import numpy as np
import math

def epsi():
 x=1
 while 1+x>1:
  x=x/2
 epsilon=2*x
 print(epsilon)
 return(epsilon)

def miseno(x):
 acu=0
 i=0
 acuant=1
 while acu != acuant:
  acuant=acu
  acu = acu + (((-1)**i)*(x**(2*i+1)))/math.factorial(2*i+1)
  print(acu)
  i=i+1
 print("el seno es", acu)
 
def miex(x):
 acu=0
 i=0
 acuant=1
 while acu != acuant:
  acuant=acu
  acu = acu + (x**i)/math.factorial(i)
  print(acu)
  i=i+1
 print("el exponencial de ",x," es", acu)
 
  
 

 