import random

class VacuumCleaner:
    def __init__(self, rows, columns):
        self.world = [['dirty' for _ in range(columns)] for _ in range(rows)]
        self.position = (random.randint(0, rows - 1), random.randint(0, columns - 1))
        self.cleaned_cells = 0

    def print_world(self):
        for row in self.world:
            print(' '.join(row))
        print()

    def is_dirty(self, row, column):
        return self.world[row][column] == 'dirty'

    def clean(self, row, column):
        if self.is_dirty(row, column):
            self.world[row][column] = 'clean'
            self.cleaned_cells += 1

    def move(self):
        row, col = self.position

        if self.is_dirty(row, col):
            self.clean(row, col)

        # Move randomly
        direction = random.choice(['left', 'right', 'up', 'down'])

        if direction == 'left' and col > 0:
            self.position = (row, col - 1)
        elif direction == 'right' and col < len(self.world[0]) - 1:
            self.position = (row, col + 1)
        elif direction == 'up' and row > 0:
            self.position = (row - 1, col)
        elif direction == 'down' and row < len(self.world) - 1:
            self.position = (row + 1, col)

def main():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    vacuum = VacuumCleaner(rows, columns)

    print("Initial World:")
    vacuum.print_world()

    while vacuum.cleaned_cells < rows * columns:
        print("Current World:")
        vacuum.print_world()
        print("Moving...")
        vacuum.move()

    print(f"The vacuum cleaner cleaned {vacuum.cleaned_cells} cells.")

if __name__ == "__main__":
    main()
