#Tienda de productos deportivos con cifrado de cesar.py

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            resultado += chr((ord(caracter) - base + desplazamiento) % 26 + base)
        else:
            resultado += caracter
    return resultado 

def desifrado_cesar(texto, desplazamiento):
    return cifrado_cesar(texto, -desplazamiento)

#Productos que estan disponibles
Productos = [
    {"id": 1, "nombre": "Balon de futbol", "precio": 25.0},
    {"id": 2, "nombre": "Raqueta de tenis", "precio": 45.0},
    {"id": 3, "nombre": "Guantes de boxeo", "precio": 35.0},
    {"id": 4, "nombre": "Zapatillas deportivas", "precio": 60.0},
]

# Carrito de compras 
carrito = []

def mostrar_productos():
    print("\nProductos disponibles")
    for p in Productos:
        print(f"{p['id']}: {p['nombre']} - ${p['precio']}")

def agregar_al_carrito(producto_id):
    producto = next((p for p in Productos if p["id"] == producto_id), None)
    if producto:
        carrito.append(producto)
        print(f"Producto agregado: {producto['nombre']}")
    else:
        print("Producto no encontrado.")

def ver_carrito():
    if not carrito:
        print("El carrito está vacío.")
        return
    print("\n Carrito actual:")
    for p in carrito:
        print(f"- {p['nombre']} - ${p['precio']}")
    total = sum(p['precio'] for p in carrito)
    print(f"Total: ${total:.2}")

def finalizar_compra():
    if not carrito:
        print("No hay nada en el carrito.")
        return
    nombre = input("Ingrese su nombre para completar la compra: " )
    nombre_cifrado = cifrado_cesar(nombre, 3)

    print("\n compra finalizada.")
    print(f"Nombre cifrado del cliente: {nombre_cifrado}")

    print(f"\n Productos cifrados comprados:")
    for p in carrito:
        nombre_prod_cifrado = cifrado_cesar(p['nombre'], 3)
        print(f"- {nombre_prod_cifrado}")

def main():
    print("Bienvenido a la tienda deportiva")
    while True:
        print("\n Opciones:")
        print("1. Ver Productos")
        print("2. Agregar al carrito")
        print("3. Ver carrito")
        print("4. Finalizar compra")
        print("5. Salir")

        opcion = input("seleccione una opción: ").strip()
        if opcion == "1":
            mostrar_productos()
        elif opcion =="2":
            try:
                id_prod = int(input("ingrese el ID del producto: "))
                agregar_al_carrito(id_prod)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "3":
            ver_carrito()
        elif opcion == "4":
            finalizar_compra()
            break
        else:
            print("Opción no válida. Intente de nuevo")

if __name__ == "__main__": 
    main ()