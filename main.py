
import Epsilon
import NoLinealFunctions
import math
import Lineal
'''
NoLinealFunctions.intervalos(-1000000,100,1)

NoLinealFunctions.bisec(-1,0)

#(a,b,max) intervalo de a-b, max de ciclos, delta 
NoLinealFunctions.reglaFalsa(-1,0)
'''

#(a,b,max) intervalo de a-b, max de ciclos, delta, tolerancia, exp en el read me 
#NoLinealFunctions.bisec(-1,0,10000) 

#NoLinealFunctions.fun(0)

#NoLinealFunctions.intervalos(-1000,1000,1)
#NoLinealFunctions.bisec(1,2,1000,0,1/3600) # si no quiero que pare por delta o pot tolerancia pongo 0 en esa entrada
#NoLinealFunctions.bisec(15,16,1000,0,1/1000000) # si no quiero que pare por delta o pot tolerancia pongo 0 en esa entrada
#NoLinealFunctions.reglaFalsa(-1,0,1000,0,0)
#NoLinealFunctions.secante(-1,-0.8,1000,0,0)

#print(Lineal.A)
#print(Lineal.parmat(Lineal.A))
Lineal.jacobi(Lineal.A, Lineal.b, Lineal.vectorinicial, 1000, 0, 0)
Lineal.SOR(Lineal.A, Lineal.b, Lineal.vectorinicial, 1000, 0, 0)

