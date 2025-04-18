def decimal_a_binario(decimal):
    try:
        # Validación de entrada
        decimal = int(decimal)
        if decimal < 0:
            return "Error: Ingresa un número decimal positivo."

        if decimal == 0:
            return "0"

        # Conversión manual de decimal a binario
        binario = ""
        while decimal > 0:
            residuo = decimal % 2
            binario = str(residuo) + binario
            decimal = decimal // 2

        return binario
    except ValueError:
        return "Error: Entrada no válida. Ingresa un número entero decimal."


def binario_a_decimal(binario):
    try:
        if not all(c in '01' for c in binario):
            return "Error: El número binario solo debe contener 0s y 1s."

        # Conversión manual de binario a decimal
        decimal = 0
        potencia = len(binario) - 1
        for digito in binario:
            decimal += int(digito) * (2 ** potencia)
            potencia -= 1

        return decimal
    except ValueError:
        return "Error: Entrada no válida. Ingresa un número binario correcto."


def menu():
    print("Conversor Decimal <-> Binario")
    print("1. Convertir Decimal a Binario")
    print("2. Convertir Binario a Decimal")
    print("3. Salir")

    while True:
        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == '1':
            numero = input("Ingresa un número decimal: ")
            resultado = decimal_a_binario(numero)
            print(f"Resultado: {resultado}\n")
        elif opcion == '2':
            numero = input("Ingresa un número binario: ")
            resultado = binario_a_decimal(numero)
            print(f"Resultado: {resultado}\n")
        elif opcion == '3':
            print("Gracias por usar el conversor. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.\n")


# Ejecutar el menú
if __name__ == "__main__":
    menu()
