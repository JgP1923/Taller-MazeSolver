class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.solution_path = []

    def find_start_and_end(self):
        startX, startY, endX, endY = None, None, None, None

        # Buscar las coordenadas de inicio y fin en los bordes del laberinto
        for x in range(self.cols):
            if self.maze[0][x] != 1:
                startX, startY = x, 0
            elif self.maze[self.rows - 1][x] != 1:
                endX, endY = x, self.rows
            if startX is not None and startY is not None and endX is not None and endY is not None:
                break

        for y in range(self.rows):
            if self.maze[y][0] != 1:
                startX, startY = 0, y
            elif self.maze[y][self.cols - 1] != 1:
                endX, endY = self.cols, y
            if startX is not None and startY is not None and endX is not None and endY is not None:
                break

        return startX, startY, endX, endY

    def solve(self):
        startX, startY, endX, endY = self.find_start_and_end()

        if startX is not None and startY is not None and endX is not None and endY is not None:
            return self._solve(startX, startY, endX, endY)
        else:
            return False

    def _solve(self, startX, startY, endX, endY):
        if startX == endX and startY == endY:
            self.solution_path.append((startX, startY))
            return True

        if (
            startX < 0
            or startX >= self.cols
            or startY < 0
            or startY >= self.rows
            or self.maze[startY][startX] == 1
        ):
            return False

        self.maze[startY][startX] = 1

        movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in movimientos:
            nextX, nextY = startX + dx, startY + dy
            if self._solve(nextX, nextY, endX, endY):
                self.solution_path.append((startX, startY))
                self.maze[startY][startX] = 0
                return True

        self.maze[startY][startX] = 0

        return False
