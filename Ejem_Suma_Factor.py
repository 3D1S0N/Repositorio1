n = int(input("Ingrese un número entero  ")) # Sumatoria de todos los enteros de 1 hasta n
suma = 0 #acumulador 
consecutivo = 1 #Genera los números de 1 hasta n 
while consecutivo <= n:
    suma = suma + consecutivo
    consecutivo = consecutivo + 1
print("La suma de los enteros de 1 hasta n es ",suma)

#Factorial de 1 hasta n
n = int(input("Ingrese un número entero  "))
factorial = 1 #acumulador
consecutivo = 1 #genera los números de 1 hasta n
while consecutivo <= n:
    factorial = factorial*consecutivo
    consecutivo = consecutivo + 1
print("El factorial de n es ",factorial)