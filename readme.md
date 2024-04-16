 
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