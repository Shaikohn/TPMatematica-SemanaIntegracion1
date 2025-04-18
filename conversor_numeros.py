def validar_decimal(decimal):
    # Validación de entrada (del número debe ser un número decimal positivo)
    if str(decimal).isdigit():
        decimal = int(decimal)
        if decimal < 0:
            return "Error: Ingresa un número entero positivo."
        return decimal
    else:
        return "Error: Entrada no válida. Ingresa un número entero positivo."
    
def validar_binario(binario):
    # Validación de entrada (el número solo debe contener 0s y 1s)
    if not all(c in '01' for c in binario):
        return "Error: El número binario solo debe contener 0s y 1s."
    return None

def decimal_a_binario(decimal):
        # Ejecuta la funcion de validacion y almacena el resultado en una variable
        validacion = validar_decimal(decimal)
        # Si la validación devuelve un string, es un error
        if isinstance(validacion, str):
             return validacion
        # Si es 0, se retorna directamente
        if decimal == 0:
           return "0"
        decimal = validacion
        # Conversión manual de decimal a binario
        binario = ""
        while decimal > 0:
            residuo = decimal % 2
            binario = str(residuo) + binario
            decimal = decimal // 2
        return binario

def binario_a_decimal(binario):
        # Ejecuta la funcion de validacion y almacena el resultado en una variable
        error = validar_binario(binario)
        if error:
           return error
        # Conversión manual de binario a decimal
        decimal = 0
        potencia = len(binario) - 1
        for digito in binario:
            decimal += int(digito) * (2 ** potencia)
            potencia -= 1
        return decimal

def menu():
    # Menu para ejecutar el programa
    print("Conversor Decimal <-> Binario")
    print("1. Convertir Decimal a Binario")
    print("2. Convertir Binario a Decimal")
    print("3. Salir")
    while True:
        opcion = input("Selecciona una opción (1/2/3): ")
        if opcion == '1':
            numero = input("Ingresa un número decimal: ")
            resultado = decimal_a_binario(numero)
            imprimir_resultado(resultado)
        elif opcion == '2':
            numero = input("Ingresa un número binario: ")
            resultado = binario_a_decimal(numero)
            imprimir_resultado(resultado)
        elif opcion == '3':
            print("Gracias por usar el conversor. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.\n") 

#Imprime el resultado de la operacion
def imprimir_resultado(resultado):
    print(f"Resultado: {resultado}\n")


# Ejecutar el menú
if __name__ == "__main__":
    menu()
