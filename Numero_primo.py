#Lea dato entero y determine si es primo o no. Número primo solo es divisible por sí mismo y la unidad.
import math
x = int(input("Ingrese un número entero  "))
i = 2 
while i <= math.sqrt(x) and x % i!=0:

    i = i+1 

if i > math.sqrt(x):

    print(x, "es primo")

else:
    
    print(x, "NO es primo")