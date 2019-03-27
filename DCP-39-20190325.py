"""
This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells.
Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates
and the number of steps it should run for. Once initialized, it should print out the board state at each step.
Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to
bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""


class Cell:

    def __init__(self, row, col):
        self.cell = (row, col)
        self.row = row
        self.col = col

    def __repr__(self):
        return str(self.cell)

    def __eq__(self, cell):
        return self.cell == cell.cell

    def __hash__(self):
        return hash(self.cell)

    @property
    def neighbors(self):
        row, col = self.cell
        return [Cell(row + 1, col),
                Cell(row - 1, col),
                Cell(row + 1, col + 1),
                Cell(row - 1, col + 1),
                Cell(row + 1, col - 1),
                Cell(row - 1, col - 1),
                Cell(row, col + 1),
                Cell(row, col - 1)]


class CGL:

    def __init__(self, live_cells):
        self.live_cells = live_cells

    def __repr__(self):
        return "\n".join(" ".join("*" if cell in self.live_cells else "." for cell in row) for row in self.sorted_cells)

    @property
    def sorted_cells(self):
        row_ends = min(cell.row for cell in self.live_cells), max(cell.row for cell in self.live_cells) + 1
        col_ends = min(cell.col for cell in self.live_cells), max(cell.col for cell in self.live_cells) + 1
        return [[Cell(row, col) for col in range(*col_ends)] for row in reversed(range(*row_ends))]

    @property
    def all_cells(self):
        return self.live_cells | set([neighbor for cell in self.live_cells for neighbor in cell.neighbors])

    def cell_lives(self, cell):
        neighbors = cell.neighbors
        live_neighbors = [neighbor for neighbor in neighbors if neighbor in self.live_cells]
        return ((2 <= len(live_neighbors) <= 3 and cell in self.live_cells) or
                (len(live_neighbors) == 3 and cell not in self.live_cells))

    def play(self, steps=10):
        for step in range(1, steps + 1):
            self.live_cells = {cell for cell in self.all_cells if self.cell_lives(cell)}
            print(f"Step {step}:")
            print(self)


a = Cell(0, 0)
cgl = CGL(set(a.neighbors + [a]))
print(cgl)
cgl.play(steps=30)
