tsa = 0
tau = 0
tns = 0
contador = 0
contAu = 0
nombre = input("Ingrese el nombre del empleado  ")
while nombre != "":
    salario = int(input(f"{nombre} ingrese el salario")
    tsa = tsa + salario
    contador = contador + 1
    aumento = 0
    if salario < 1000:
        aumento = salario * 0.1
        tau = tau + aumento 
        contAu = contAu + 1
    nuevoSalario = salario + aumento 
    tns = tns + nuevoSalario
    print("Nombre", nombre, "\tsalario", salario, "\taumento\t", aumento, "\tNuevo salario\t", nuevoSalario)
    nombre = input ("Ingrese el nombre del empleado  ")
psa = tsa / contador
pau = tau / contador
pns = tns / contador
print("Total empleados", contador, "\tTotal con aumento > cero", contAu)
print("Total salarios anteriores\t", tsa, "\tPromedio\t", psa)
print("Total aumentos           \t", tau, "\tPromedio\t", pau)
print("Total nuevos salarios    \t", tna, "\tPromedio\t", pns)
