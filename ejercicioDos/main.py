from Escuderia import Escuderia

escuderias = []
contador = 1
numeroEscuderias = int(input("Digite el numero de escuderias: "))
while contador <= numeroEscuderias:
    escuderia = Escuderia()
    escuderia.nombre = input("digite el nombre de la escuderia: ")
    escuderia.casaMotor = input("digite el nombre del casamotor: ")
    escuderia.pilotoPrincipal.nombre = input("digita el nombre del piloto: ")
    escuderia.pilotoPrincipal.salarioAnual = int(input("digita el salario del piloto: "))
    escuderia.pilotoPrincipal.fechaNacimiento = input("digita la fecha de nacimiento del piloto: ")
    escuderia.pilotoPrincipal.pais = input("digita el pais: ")
    escuderia.piloto2.nombre = input("digita el nombre del copiloto: ")
    escuderia.piloto2.salarioAnual = int(input("digita el salario del copiloto: "))
    escuderia.piloto2.fechaNacimiento = input("digita la fecha de nacimiento del copiloto: ")
    escuderia.piloto2.pais = input("digita el pais del copiloto: ")
    escuderia.costos = int(input("ingrese los costos: "))
    #Incrementando contador
    contador = contador + 1
    escuderias.append(escuderia)



# Recorriendo la Lista de escuderías
costoMayor = 0
nombreEscuderiaMasCara = None
for escuderia in escuderias:
    print(escuderia.nombre, escuderia.costos)
    

for escuderia in escuderias:
    if escuderia.costos > costoMayor:
        costoMayor = escuderia.costos
        nombreEscuderiaMasCara = escuderia.nombre

print(f"La escuderia mas cara es {nombreEscuderiaMasCara}")
