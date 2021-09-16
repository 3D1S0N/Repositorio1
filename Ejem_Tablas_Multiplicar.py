#Tabla de multiplicar. Lea entero n e imprima tablas de n desde 1 hasta 10.
n = int(input("Ingrese un número entero "))
i = 1
while i<=10:
    r = n*i
    print(n,"*",i,"=",r)
    i=i+1
print("terminé\n")

n = int(input("Ingrese un número entero "))
x = 1
while x<=n:
    i = 1

    while i <= 10:
        r = x*i  
        print(x,"*",i,"=",r)
        i=i+1
    x = x +1 
    print("")