#Elabore un programa en Python que lea un entero de dos dígitos y produzca como salida los dígitos del número leído con su correspondiente
# mensaje. Por ejemplo, si el número leído es 27, la salida deberá ser:(sin texto adicional):
#2
#7

lista = []
def numero(dosdigitos):
    for i in dosdigitos:
        lista.append(int(i))
    print(lista[0])
    print(lista[1])
    
usuario = input("Ingrese un número entero de dos dígitos:  ")
numero(usuario)

