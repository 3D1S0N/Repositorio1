ingenieros = medicos = abogados = otros = 0
nombre = input("Teclee su nombre  ")
profesion = int(input(f"{nombre} entre profesion:   "))
if profesion == 1:
    ingenieros = ingenieros + 1
elif profesion == 2:
    medicos = medicos + 1
elif profesion == 3:
    abogados = abogados + 1
else:
    otros = otros + 1
print("Ingenieros:  ", ingenieros, "\nMedicos:", medicos, "\nAbogados:", abogados, "\notros", otros)



