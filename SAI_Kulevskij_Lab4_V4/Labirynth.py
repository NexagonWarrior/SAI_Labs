import random
import os


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['#' for _ in range(width)] for _ in range(height)]
        self.start_pos = (1, 0)
        self.exit_pos = (width - 1, height - 2)
        self._generate()

    def _generate(self):
        def walk(x, y):
            self.grid[y][x] = ' '
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random.shuffle(dirs)
            for dx, dy in dirs:
                nx, ny = x + dx * 2, y + dy * 2
                if 0 <= nx < self.width and 0 <= ny < self.height and self.grid[ny][nx] == '#':
                    self.grid[y + dy][x + dx] = ' '
                    walk(nx, ny)

        walk(1, 1)
        self.grid[self.start_pos[1]][self.start_pos[0]] = ' '
        self.grid[self.exit_pos[1]][self.exit_pos[0]] = ' '

    def is_wall(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x] == '#'
        return True

    def draw(self, player_pos):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if (x, y) == player_pos:
                    row += "P "
                elif (x, y) == self.exit_pos:
                    row += "E "
                else:
                    row += "██" if self.grid[y][x] == '#' else "  "
            print(row)


class Player:
    def __init__(self, start_pos):
        self.x, self.y = start_pos

    @property
    def pos(self):
        return (self.x, self.y)

    def move(self, dx, dy, maze):
        nx, ny = self.x + dx, self.y + dy
        if not maze.is_wall(nx, ny):
            self.x, self.y = nx, ny
            return True
        return False


class Game:
    def __init__(self, width=25, height=25):
        self.maze = Maze(width, height)
        self.player = Player(self.maze.start_pos)
        self.running = True

    def run(self):
        while self.running:
            self.maze.draw(self.player.pos)
            print(f"Координати: {self.player.pos} | Ціль: {self.maze.exit_pos}")

            command = input("WASD для руху, Q для виходу: ").lower()

            if command == 'q':
                self.running = False
                continue

            dx, dy = 0, 0
            if command == 'w':
                dy = -1
            elif command == 's':
                dy = 1
            elif command == 'a':
                dx = -1
            elif command == 'd':
                dx = 1

            self.player.move(dx, dy, self.maze)

            if self.player.pos == self.maze.exit_pos:
                self.maze.draw(self.player.pos)
                print("\nВІТАЮ! Ви пройшли лабіринт!")
                self.running = False


if __name__ == "__main__":
    game = Game(25, 25)
    game.run()