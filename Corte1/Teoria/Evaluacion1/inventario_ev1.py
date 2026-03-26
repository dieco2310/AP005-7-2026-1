# ==============================
# SISTEMA DE INVENTARIO SIMPLE
# ==============================

# 1. Tupla (información fija del sistema)
categorias = ("Vapes", "Snacks(munchies :>)", "Bebidas(Pa´ la seca)", "Productos varios")

# 2. Lista para almacenar productos
inventario = []

# 3. Mensaje de bienvenida
print("=== BIENVENIDO AL SISTEMA DE INVENTARIO ===")

# Función para agregar producto
def agregar_producto():
    print("\n--- Agregar Producto ---")
    
    codigo = input("Ingrese código: ")
    nombre = input("Ingrese nombre: ")
    
    # Validación de precio
    while True:
        try:
            precio = float(input("Ingrese precio: "))
            break
        except:
            print("Error: Ingrese un número válido")
    
    # Validación de cantidad
    while True:
        try:
            cantidad = int(input("Ingrese cantidad: "))
            break
        except:
            print("Error: Ingrese un número entero válido")
    
    print("Categorías disponibles:", categorias)
    categoria = input("Ingrese categoría: ")
    
    # Diccionario del producto
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
    }
    
    inventario.append(producto)
    print("Producto agregado correctamente.")

# Función para mostrar productos
def mostrar_productos():
    print("\n--- Lista de Productos ---")
    
    if len(inventario) == 0:
        print("No hay productos.")
    else:
        for producto in inventario:
            print(producto)

# Función para buscar producto
def buscar_producto():
    print("\n--- Buscar Producto ---")
    codigo = input("Ingrese código a buscar: ")
    
    for producto in inventario:
        if producto["codigo"] == codigo:
            print("Producto encontrado:", producto)
            return
    
    print("Producto no encontrado.")

# Función para eliminar producto
def eliminar_producto():
    print("\n--- Eliminar Producto ---")
    codigo = input("Ingrese código a eliminar: ")
    
    for producto in inventario:
        if producto["codigo"] == codigo:
            inventario.remove(producto)
            print("Producto eliminado.")
            return
    
    print("Producto no encontrado.")

# 4. Menú principal con while
while True:
    print("\n=== MENÚ ===")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    # 5. Condicionales
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida.")
