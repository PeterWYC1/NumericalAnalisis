 
criterios de parada

1. max de ciclos (caso pesimista)

2. criterio delta: 
 seleccionamos un num delta posítivo lo suficientemente pequeño 
 con el cual podemos suponer que: abs(F(x)<= delta)
 
3. Criterio de tolerancia 
 seleccionamos un num suficientemente pequeño que si el 
 error<= que la tolerancia 

 Mayor exigencia es TOL=0 DELTA=0
 
 EJEMPLO EXAMEN

 El volumen de liquido (en m^3) dentro de un tanque de gran tamaño cambia en el tiempo (en horas) según la función:
   
  V(t)+ 600+17t^2-cos(8t)

 Tiempo necesario para que el liquido se duplique teniendo en cuenta que su respuesta debe asegurar su calidad en segundos. 

 Solucion:
  En t=o el volumen es : 600+0+cos(0)=599
  Entonces queremos encontrar el tiempo en segundos cuanto V= 1198

   tenemos   600+17t^2-cos(8t)=1198 la volvemos forma F(t)=0

la precicion de segundos determina el criterio de parada para el error unidades de la t, lo que está en la funcion, ent hacemos la convercion y hacemos el criterio de parada en la tolerancia 

si me dijeran precicion del volumen ej millonecima de volumen estaria en las unidades de la F, ahora el citerio es de la F ent cambiamos el delta

MIRAR FOTO PARA VER CONVERSIONES 

LOS CRITERIOS DE PARADA LOS DA EL PROBLEMA


Ej: F(t)=0
F(t) en newtons
t en KM

si nos dijeran que la respuesta debe garantizar calidad de milimetros(criterio de tolerancia)
si error = 1km
precicion de milimetros : tolerancia=1/1.000.000 (esto seria pq si el error es menor a un milimetro ya tendriamos una precicion de milimetros)

si debemos garantizar una precicion de 10 millonecima de newton 
 f(t)=1 newton 
 delta = 1/10.000.000 precicion de diez millonecima de newton

Guardar docs con ApellidoNombre

SI NO NOS DICEN QUE MERODO USAR USAMOS SECANTE 

RAPIDEZ DE CONVERGENCIA (la cantidad de ceros del error dependen de la convergencia, más ceros más rápido es mejor) 

   Bisección     |
   Regla Falsa   | (Convergencia lineal)
   Punto fijo    |
   (E(n) es proporcinal  E(n-1)^1)


   Newton Rapzon (Convergencia cuadratica)
   (E(n) es proporcional a E(n-1)^2 si un num pequeño se eleva a la dos se vuelve más pequeño)
   el error disminuye más fast

   Secante (Convergencia aúrea)
   (E(n) es proporcional a E(n-1)^((1+5^1-2)/2) este numero del exponente es aprox 1.6 el cual es el numero de oro)

   El metodo de secante excelecia para busqueda de funciones NO lineales

   METODO SPLINE LINEAL

  dada una lista de puntos (Xi , Yi) ordenados de menor a mayor en la variablre "X" se encuentra una recta 
  y = mX + b la  cual se encuentra para cada tramo 
   
   - X0 <= X <= X1
   - X1 <= X <= X2
   - X2 <= X <= X3
   - X3 <= X <= Xn

   despues de hacer spline en el excel se hace una grafica donde no se vean los cambios entre intervalos, se unen las rectas con polinomios aplicando splien cubico 

   SPLINE CÚBICO 

   dada una lista de puntos (Xi , Yi) ordenados de menor a mayor en la variablre "X" se encuentra un polinomio cúbico tipo ax^3+bx^2+cx+d el cual se encuentra para cada tramo 

   - X0 <= X <= X1
   - X1 <= X <= X2
   - X2 <= X <= X3
   - X3 <= X <= Xn
   
   FOTO EJEMPLO EN CELULAR

   1) donde se cumple que cada polinomio pasa por los dos puntos que le corresponde:

      Ej: el primero tiene que pasar por (Xo ,Yo) y por  (X1 ,Y1) y así con todos los otros 

   2) la pendiente de dos puntos consecutivos es igual en su punto de empalme,  cuando un tramo se conecta en el punto que tienen igual su pendiente es la misma

   3) la concavidad en el punto de encuentro de dos tramos es el mismo 

   4) el punto inicial y final (extremos) deben cumplir condiciones NATURALES o sujetas 

   El sistema de escuaciones que vamos a encontrar con el spline's cúbico con los codigos que tenemos, es recomendado usar SOR porque este se le puede cambiar la W y si no converge se reorganizan las filas hasta que converga 

   ejemplo en celular

   Pasos: 
      1) nos dan los puntos y los organizamos de menor a mayor 
      2) se plantea el polinomio con los intervalos definidos
      3) se forma la matriz de incognitas de tamaño n-1 * 4 (n = cantidad de puntos)
      4) la segunda condición me dice que la pendiente debe ser igual en los puntos de empalme entonces planteo esas ecuaciones 
      5) las concavidades deven ser la misma en el empalme ent se plantean las ecuaciones con las segundas derivadas
      6) los extremos cumplen condiciones natruales o las sujetas:
         - Un punto cumple la condición natural, si su segunda derivada es = 0 entonces es las ecuaciones de concavidad evaluadas en las x de el primer y ultimo punto en su respectiva ecuación y estas = 0 por la condicion dada.

         - Un punto cumple una condicion sujeta si al inicio se dio información adicional sobre el
         como : en el primer punto la pendiente debe valer 14,  son condiciones dadas para los extremos

         - (si solo nos dan una sujeta en el otro punto debe ser condición natural)
      7) la recomendación es reoraganizar la matiz para que en la digaonal PPL no hayan ceros
      8) se encuentra el vector B 
      REVISAR MOODLE PARA CÚBICOS CON POLINOMIOS TRANSLADADOS 