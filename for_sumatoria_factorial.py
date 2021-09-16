#suma de los enteros desde 1 hasta n 
n = int(input("Ingrese un número entero  "))
suma = 0
for i in range(1, n+1, 1): #(valorinicial, valor final, variación)
    suma = suma + i 
print("La suma de los enteros de 1 hasta", n, "es", suma)

#factorial de 1 hasta n
n = int(input("Ingrese un número entero  "))
factorial = 1
for i in range(1, n+1, 1): #(valorinicial, valor final, variación)
    factorial = factorial*i 
print("El factorial de", n, "es", factorial)
