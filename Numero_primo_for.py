x = int(input("Ingrese un número entero "))
if x % 2 == 0:
    print(x, "NO es primo, es número par")
    exit(0)
i = 2 
for i in range(3, int(x**(0.5))+1, 2):
    if x % i== 0:
        print(x, "NO es primo, es divisible por", i)
        break
if x % i != 0:
    print(x, "es primo")

