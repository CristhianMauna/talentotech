import math

# FUNCIONES BÁSICAS
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: no se puede dividir por cero"

# FUNCIONES CIENTÍFICAS
def seno(a):
    return math.sin(math.radians(a))

def coseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def logaritmo(a):
    if a > 0:
        return math.log(a)
    else:
        return "Error: el número debe ser positivo"

# FUNCIÓN PARA ALMACENAR DATOS
def almacenar_datos():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    grado_estudio = input("¿Cuál es su grado de estudio actual?: ")
    return nombre, edad, grado_estudio

# FUNCION PRINCIPAL
def calculadora():
    nombre, edad, grado_estudio = almacenar_datos()
    print(f"\n¡Bienvenido {nombre} de {edad} años, que cursa {grado_estudio}!")

    while True:
        print("\nSeleccione la operación:")
        print("1. SUMAR")
        print("2. RESTAR")
        print("3. MULTIPLICAR")
        print("4. DIVIDIR")
        print("5. SENO")
        print("6. COSENO")
        print("7. TANGENTE")
        print("8. LOGARITMO (base e)")
        print("q. SALIR")

        opcion = input("Ingrese el número de la operación (1-8) o 'q' para salir: ")

        if opcion.lower() == 'q':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == '1':
                print(f"Resultado: {num1} + {num2} = {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {num1} - {num2} = {restar(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif opcion == '4':
                print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")

        elif opcion in ['5', '6', '7', '8']:
            num = float(input("Ingrese el número (en grados para funciones trigonométricas): "))

            if opcion == '5':
                print(f"Resultado: seno({num}) = {seno(num)}")
            elif opcion == '6':
                print(f"Resultado: coseno({num}) = {coseno(num)}")
            elif opcion == '7':
                print(f"Resultado: tangente({num}) = {tangente(num)}")
            elif opcion == '8':
                print(f"Resultado: logaritmo({num}) = {logaritmo(num)}")

        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar
calculadora()