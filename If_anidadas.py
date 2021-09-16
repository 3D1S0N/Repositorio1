nombre = input("Ingrese el nombre:    ")
genero = int(input("Ingrese el género:    "))
estatura = int(input("Ingrese la estatura:    "))
peso = int(input("Ingrese el peso:    "))
if estatura > 180:
    if peso > 70:
        if genero == 0:
            print("Reina de belleza")
        else:
            print("Cantautor")
    else:
        print("Arbitro de fútbol")
else:
    print("Jugador de parqués")
print("Paciente clasificado")