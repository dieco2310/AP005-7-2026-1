############### LISTAS ################
# Las listas se crean con [] y permiten guardar varios datos

colores = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

print(colores)
print(type(colores))  # Verificamos que sea tipo lista
print(colores[2])     # Tercer elemento

# Cantidad de elementos
print("Cantidad de elementos:", len(colores))

# Sublistas (slicing)
print(colores[0:2])   # Desde posición 0 hasta antes de la 2
print(colores[:2])    # Forma equivalente

# Agregar elementos
colores.append('Blanco')
print(colores)

# Insertar en una posición específica
colores.insert(3, 'Negro')
print(colores)

# Añadir varios elementos desde otra lista
colores += ['Marron', 'Gris']
print(colores)

# Buscar posición de un elemento
print("Índice de Azul:", colores.index('Azul'))

# Eliminar un elemento específico
colores.remove('Marron')
print(colores)

# Insertar nuevamente
colores.insert(8, 'Marron')
print(colores)

# Eliminar último elemento
ultimo = colores.pop()
print("Elemento eliminado:", ultimo)

# Tamaño actual
print("Total elementos:", len(colores))

# Repetir lista
lista_repetida = colores * 3
print("Lista repetida:", lista_repetida)

# Ordenamiento
print("\nOrdenando lista de colores:")
colores.sort()
print(colores)

# Lista numérica
numeros = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("\nOrden ascendente:")
numeros.sort()
print(numeros)

print("Orden descendente:")
numeros.sort(reverse=True)
print(numeros)


############### TUPLAS EN PYTHON ################
# Son similares a listas pero no se pueden modificar

print("\n########### TUPLAS ###########")

# Convertir lista a tupla
tupla_colores = tuple(colores)
print("Tupla:", tupla_colores)

# Acceso por índice
print(tupla_colores[0])
print(tupla_colores[2])

# Verificar existencia
print('Rojo' in tupla_colores)

# Contar ocurrencias
print("Cantidad de 'Rojo':", tupla_colores.count('Rojo'))

# Tupla de un solo elemento
tupla_unica = ('Blanco',)
print(tupla_unica)

# Crear tupla sin paréntesis
datos = 'Gaspar', 5, 8, 1999
print(datos)

# Desempaquetado
nombre, dia, mes, anio = datos
print(nombre)
print(dia)
print(mes)
print(anio)

print(f"Nombre: {nombre} - Día: {dia} - Mes: {mes} - Año: {anio}")

# Convertir tupla a lista
lista_convertida = list(datos)
print(lista_convertida)