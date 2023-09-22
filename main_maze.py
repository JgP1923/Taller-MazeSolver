import csv

# Nombre del archivo CSV que deseas abrir
archivo_csv = "maze.csv"

# Inicializar una lista para almacenar la matriz del laberinto
maze = []

# Abrir el archivo CSV en modo lectura
with open(archivo_csv, mode="r") as file:
    # Crear un lector CSV
    reader = csv.reader(file)
    
    # Iterar a través de las filas del archivo CSV
    for fila in reader:
        # Convertir los valores de la fila a enteros y agregarlos a la matriz
        fila_enteros = [int(valor) for valor in fila]
        maze.append(fila_enteros)