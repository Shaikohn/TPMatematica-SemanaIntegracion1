## Este programa pedira al usuario un numero decimal, lo convertira a binario y viceversa ##

# Desplegamos una especie de menu
print("ingrese una opcion: ")
print("1) dec a bin")
print("2) bin a dec")

# almacenamos la opcion que elija el usuario
opcion = int(input())

# si selecciona la opcion 1
if opcion == 1:
    num = int(input("ingrese un numero: ")) # almacenamos el numero decimal del usuario
    bin = ""                                # variable para almacenar el numero binario
    # mientras el numero sea mayor que cero, hacemos las divisiones almacenando los restos para cargarlos en la variable bin
    while num > 0:
        if num % 2 == 0:
            bin = "0" + bin
        else:
            bin = "1" + bin
        num = num // 2
    print(bin)                              # imprimimos el resultado

# si selecciona la opcion 2
elif opcion == 2:
    bin = input("ingrese el numero: ")      # almacenamos el nmero binario como un string
    # nos aseguramos de que el numero sea binario
    for x in range(len(bin)):
        if bin[x] != "1" and bin != "0":
            print("ese no es un numero binario.")
            break
        else:
            break
        
    dec = 0                                 # creamos la variable dec para almacenar el resultado de la traduccion
    largo = len(bin)                        # usamos el largo pra dar vuelta el numero
    # el parametro reversed, hace que el for recorra el numero de derecha a izquierda
    for x in reversed(bin):
        if x == "1":
            # aca hacemos la suma de potencias con base 2 para la conversion
            dec = dec + (2 ** (len(bin) - largo))   
        largo = largo - 1                   # cada ciclo, restamos uno al valor de largo para que el civlo avance
    print(dec)                              # imprimimos el resultado
# si el usuario no ingresa ni un 1 ni un 2, imprimimos el siguente mensaje

else:
    print("no es una opcion valida.")