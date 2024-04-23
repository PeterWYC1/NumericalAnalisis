import numpy as np
#Matriz A
A=np.array([[]])
#np.array([[8,-2,3],[5,-9,1],[7,2,-14]])

#Vector de resultados
b=np.array([[-5],[2],[0]])

#Vector Inicial
vectorinicial=np.array([[2],[15],[1]])

#como se parte la matriz  A  en las matrices  D ,  L  y  U .
def parmat(M):
  numfilas=len(M)
  D=np.zeros((numfilas,numfilas))
  L=np.zeros((numfilas,numfilas))
  U=np.zeros((numfilas,numfilas))

  for i in range(numfilas):
    for j in range(numfilas):
      if i==j:
        D[i,j]=M[i,j]
      if i<j:
        U[i,j]=-M[i,j]
      if i>j:
        L[i,j]=-M[i,j]
  return(D,L,U)
 
def jacobi(M,vecind,X0,nmax,delta,tole):
  F=parmat(M)
  D=F[0]
  L=F[1]
  U=F[2]
  DI=np.linalg.inv(D)
  T=DI @ (L+U)
  print('Los valores propios de T son:')
  print(np.abs(np.linalg.eigvals(T)))
  C=DI @ vecind

  i=0
  fx=delta+1
  error=tole+1
  while i<nmax and fx>delta and error>tole:
    i=i+1
    print('El ciclo es:',i)
    X=(T @ X0)+C
    np.set_printoptions(formatter={'float_kind':"{:.17f}".format})
    print('X:', X)
    fx=np.linalg.norm(M @ X-vecind)
    print('fx es:', fx)
    error=np.linalg.norm(X-X0)
    print('El error es:', error)
    print('----------------------------')
    X0=X

def gauss_seidel(M, vecind, X0, nmax, delta, tole):
  F = parmat(M)
  D = F[0]
  L = F[1]
  U = F[2]
  DI = np.linalg.inv(D-L)
  T = DI @ U
  print('Los valores propios de T son:')
  print(np.abs(np.linalg.eigvals(T)))
  C = DI @ vecind

  i = 0
  fx = delta + 1
  error = tole +1
  while i<nmax and fx > delta and error > tole:
    i = i+1
    print('El ciclo es: ', i)
    X = (T @ X0) + C
    print('X es: ', X)
    fx = np.linalg.norm(M@X - vecind)
    print('fx es: ', fx)
    error = np.linalg.norm(X-X0)
    print('El error es: ', error)
    print('-----------------------')
    X0=X
   
def castano(M, vecind, X0, nmax, delta, tole):
  F = parmat(M)
  D = F[0]
  L = F[1]
  U = F[2]
  DI = np.linalg.inv(D-1/4*L-1/3*U)
  T = DI @ (3/4*L+2/3*U)
  print('Los valores propios de T son:')
  print(np.abs(np.linalg.eigvals(T)))
  C = DI @ vecind

  i = 0
  fx = delta + 1
  error = tole +1
  while i<nmax and fx > delta and error > tole:
    i = i+1
    print('El ciclo es: ', i)
    X = (T @ X0) + C
    print('X es: ', X)
    fx = np.linalg.norm(M@X - vecind)
    print('fx es: ', fx)
    error = np.linalg.norm(X-X0)
    print('El error es: ', error)
    print('-----------------------')
    X0 = X 
 
 
    
def richardson(M, vecind, X0, nmax, delta, tole):
  filas = len(M)
  T = np.eye(filas) - M
  print('Los valores propios de T son:')
  print(np.abs(np.linalg.eigvals(T)))
  C = vecind
  
  i = 0
  fx = delta + 1
  error = tole +1
  while i<nmax and fx > delta and error > tole:
    i = i+1
    print('El ciclo es: ', i)
    X = (T @ X0) + C
    print('X es: ', X)
    fx = np.linalg.norm(M@X - vecind)
    print('fx es: ', fx)
    error = np.linalg.norm(X-X0)
    print('El error es: ', error)
    print('-----------------------')
    X0=X
    
   
def SOR(M, vecind, X0, nmax, delta, tole,w):
  F = parmat(M)
  D = F[0]
  L = F[1]
  U = F[2]
  DI = np.linalg.inv(D-w*L)
  T = DI @ ((1-w)*D+w*U)
  print('Los valores propios de T son:')
  print(np.abs(np.linalg.eigvals(T)))
  C = w*DI @ vecind

  i = 0
  fx = delta + 1
  error = tole +1
  while i<nmax and fx > delta and error > tole:
    i = i+1
    print('El ciclo es: ', i)
    X = (T @ X0) + C
    print('X es: ', X)
    fx = np.linalg.norm(M@X - vecind)
    print('fx es: ', fx)
    error = np.linalg.norm(X-X0)
    print('El error es: ', error)
    print('-----------------------')
    X0 = X 

 
  
  