import tkinter as tk
from tkinter import messagebox
from main_maze import maze
from maze_solver import MazeSolver

ventana = tk.Tk()
ventana.title("Laberinto")

mazeImportado = maze

lienzo = tk.Canvas(ventana, width=500, height=500)
lienzo.pack()

def dibujar_maze():
    for fila in range(len(mazeImportado)):
        for columna in range(len(mazeImportado[fila])):
            x1 = columna * 45
            y1 = fila * 45
            x2 = x1 + 45
            y2 = y1 + 45

            if mazeImportado[fila][columna] == 0:
                color = "white"
            else:
                color = "green"
            lienzo.create_rectangle(x1, y1, x2, y2, fill=color)

def encontrar_todos_los_caminos():
    def backtrack(x, y):
        if x == endX and y == endY:
            solution_paths.append(list(solution_path))
            return

        if (
            x < 0
            or x >= cols
            or y < 0
            or y >= rows
            or mazeImportado[y][x] == 1
            or visited[y][x]
        ):
            return

        visited[y][x] = True
        solution_path.append((x, y))

        backtrack(x + 1, y)
        backtrack(x - 1, y)
        backtrack(x, y + 1)
        backtrack(x, y - 1)

        solution_path.pop()
        visited[y][x] = False

    rows = len(mazeImportado)
    cols = len(mazeImportado[0])
    visited = [[False] * cols for _ in range(rows)]
    solution_paths = []
    solution_path = []

    startX, startY, endX, endY = MazeSolver(mazeImportado).find_start_and_end()

    if startX is not None and startY is not None and endX is not None and endY is not None:
        backtrack(startX, startY)

        if solution_paths:
            messagebox.showinfo(title="Laberinto", message=f"Se encontraron {len(solution_paths)} soluciones.")
            
            def mostrar_siguiente_camino():
                nonlocal current_solution
                if current_solution < len(solution_paths):
                    lienzo.delete("all")
                    dibujar_maze()
                    path = solution_paths[current_solution]
                    for x, y in path:
                        x1 = x * 45
                        y1 = y * 45
                        x2 = x1 + 45
                        y2 = y1 + 45
                        lienzo.create_rectangle(x1, y1, x2, y2, fill="red")
                    current_solution += 1
                else:
                    messagebox.showinfo("Laberinto", "Todos los caminos han sido mostrados.")

            current_solution = 0
            boton_siguiente_camino = tk.Button(ventana, text="Siguiente Camino", command=mostrar_siguiente_camino)
            boton_siguiente_camino.pack()

boton = tk.Button(ventana, text="Dibujar Maze", command=dibujar_maze)
boton.pack()

boton_auto = tk.Button(ventana, text="Encontrar Todos los Caminos", command=encontrar_todos_los_caminos)
boton_auto.pack()

ventana.mainloop()