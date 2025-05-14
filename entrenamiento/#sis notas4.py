# Diccionario para almacenar la información de cada estudiante
# Clave: nombre (str), Valor: tupla (lista de notas, promedio)
estudiantes = {}

while True:
    print("\n--- Sistema de Notas ---")
    nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")

    if nombre.lower() == 'salir':
        break

    #Lista temporal para guardar las notas
    notas = []
    i = 1
    while True:
        nota_input = input(f"Ingrese la nota #{i} para {nombre} (o 'fin' para terminar): ")
        if nota_input.lower() == 'fin':
            break
        try:
            nota = float(nota_input)
            if 0 <= nota <=10:
                notas.append(nota)
                i += 1
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.") 

    if notas:
        promedio = sum(notas) / len(notas)
        estudiantes[nombre] = (notas, promedio)
        print(f"Notas de {nombre} registradas con éxito. Promedio: {promedio:.2f}")
    else:
        print("No se ingresaron notas válidas.")

#Mostrar resumen
print("\n --- Resumen de Notas ---")
for nombre, (notas, promedio) in estudiantes.items():
    print(f"Estudiantes: {nombre}")
    print(f"  Notas: {notas}")
    print(f"  Promedio: {promedio:.2f}")
