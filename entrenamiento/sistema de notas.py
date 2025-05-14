#Sistema de Notas Universidad 

def mostrar_materias(materias):
    print("\nMaterias disponibles:")
    for i, materia in enumerate(materias, 1):
        print(f"{i}. {materia}")

def ingresar_nota():
    while True:
        try:
            nota = float(input("Ingrese la nota (0.0 - 10.0): "))
            if 0.0 <= nota <= 10.0:
                return nota
            else:
                print("La nota debe estar entre 0.0 y 10.0.")
        except ValueError:
            print("Entrada inválida. Ingrese un valor numérico.")

def mostrar_registro(notas_estudiantes):
    print("\n--- Registro Final de Notas ---")
    for estudiante, lista_notas in notas_estudiantes.items():
        print(f"\nEstudiante: {estudiante}")
        total = 0
        for materia, nota in lista_notas:
            print(f"  {materia}: {nota}")
            total += nota
        promedio = total / len(lista_notas) if lista_notas else 0
        print(f"  Promedio general: {promedio:.2f}")

def sistema_notas():
    materias = ["Matemáticas", "Física", "Programación", "Química", "Historia"]
    notas_estudiantes = {}

    while True:
        print("\n--- Sistema de Gestión de Notas Universitarias ---")
        nombre = input("Ingrese el nombre del estudiante (o 'salir' para finalizar): ").strip()

        if nombre.lower() == "salir":
            break

        if nombre not in notas_estudiantes:
            notas_estudiantes[nombre] = []

        mostrar_materias(materias)
        materia = input("Ingrese el nombre de la materia: ").strip()

        if materia not in materias:
            print("La materia ingresada no está en la lista disponible.")
            continue

        nota = ingresar_nota()
        notas_estudiantes[nombre].append((materia, nota))
        print(f"Nota registrada exitosamente para {nombre} en {materia}.")

    mostrar_registro(notas_estudiantes)

# Ejecutar el programa
if __name__ == "__main__":
    sistema_notas()