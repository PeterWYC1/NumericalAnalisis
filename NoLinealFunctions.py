# imports needed
import numpy as np
import math
import pandas as pd

# ingresemos la función F(x)
def fun(x):
 g=9.81 #gravedad 
 r=math.exp(3*x) - 5*x**2 + math.sin(7*x) - 2*x - math.cos(x) + 4 
 # (de esta funcion se despejo la x para el metodo de punto fijo)
 #r=x**17-0.001
 #r=(x**3)-(0.73200760*x**2)-(1.999912*x)-1.463912
 #r=(3*x**2)-math.exp(x)
 #r=600+(17*x**2)-math.cos(8*x)-1198
 #r=(((g*x)/15)*(1-math.exp(-(15/x)*10)))-36
 #r=(-1*((x/100)**4)+math.exp((7*x)/100)+2-5) 
 # r=((math.sqrt(2*g*x))*(math.tan(2.5*math.sqrt(2*g*x)/8)))-5
 return(r)


euleralados = math.exp(2)


# función para encontrar el intervalo de signo 
def intervalos(a,b,paso):
 while a<b:
  if fun(a)*fun(a+paso)<0:
   print(a,a+paso)
  a=a+paso
  
   
def bisec(a,b,max,delta,tol):
 i=0
 y=1
 error=1
 tabla=[]
 xant=a #para que no sea la misma ponemos a 
 while i<max and abs(y)>delta and error>tol and y!=0 and error!=0:
  i=i+1
  x=(a+b)/2
  y=fun(x)
  error=abs(x-xant)
  if fun(a)*fun(x)<0:
   b=x
  else:
   a=x
  xant=x
  tabla.append([i,x,y,error])
 h = pd.DataFrame(tabla, columns=['Contador', 'x', 'f(x)', 'error_absoluto'])
 h = h.set_index('Contador')
 pd.set_option('display.float_format', '{:.17f}'.format)
 print(h)  
 
 # regla falsa es mejor segun la funcion, si se parece más a una recta es mejor
 # si no se parece casi a una recta biseccion es más eficiente

def reglaFalsa(a,b,max,delta,tol):
 i=0
 y=1
 error=1
 tabla=[]
 xant=a #para que no sea la misma ponemos a 
 while i<max and abs(y)>delta and error>tol and y!=0 and error!=0:
  i=i+1
  x=b-(fun(b)*(b-a))/(fun(b)-fun(a))
  y=fun(x)
  error=abs(x-xant)
  if fun(a)*fun(x)<0:
   b=x
  else:
   a=x
  xant=x
  tabla.append([i,x,y,error])
 h = pd.DataFrame(tabla, columns=['Contador', 'x', 'f(x)', 'error_absoluto'])
 h = h.set_index('Contador')
 pd.set_option('display.float_format', '{:.17f}'.format)
 print(h)  
 
 
# criterios de parada

# 1) max de ciclos (caso pesimista)

# 2) criterio delta: 
# seleccionamos un num delta posítivo lo suficientemente pequeño 
# con el cual podemos suponer que: abs(F(x)<= delta)

# 3)

def g(x):
 r=-math.sqrt((math.exp(3*x)+math.sin(7*x)-2*x-math.cos(x)+4)/5)
 # en el metodo de newton rapzon se cambia g(x) no por la funcion despejada en una x 
 #si no por g(x) = x - f(x) / f'(x) 
 return(r)

# Problemas con newton rapzon, a veces no vale la pena hacer la derivada 
# Si la derivada se vuelve cero 
# se usa el metodo de punto fijo pero 

def puntof(a,nmax,delta,tole):
  i=0
  y=1
  xant=a
  error=1
  tabla=[]
  while i<nmax and abs(y)>delta and error > tole:
    i=i+1
    x=g(a)
    y=fun(x)
    error = abs(x-xant)
    a=x
    xant=x
    tabla.append([i,x,y,error])
  h = pd.DataFrame(tabla, columns=['contador','x', 'f(x)', 'error absoluto'])
  h = h.set_index('contador')
  pd.set_option('display.float_format', '{:.17f}'.format)
  print(h)
 

def secante(a,b,max,delta,tol): # a y b se vuelven cualquier numero del intervalo
 i=0
 y=1
 error=1
 tabla=[]
 while i<max and abs(y)>delta and error>tol and y!=0 and error!=0:
  i=i+1
  x=b-(fun(b)*(b-a))/(fun(b)-fun(a))
  y=fun(x)
  error=abs(x-b)
  a=b 
  b=x
  tabla.append([i,x,y,error])
 h = pd.DataFrame(tabla, columns=['Contador', 'x', 'f(x)', 'error_absoluto'])
 h = h.set_index('Contador')
 pd.set_option('display.float_format', '{:.17f}'.format)
 print(h)   
 

 