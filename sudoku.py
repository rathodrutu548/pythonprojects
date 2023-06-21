import random

# Generate a complete Sudoku grid
def generate_grid():
    numbers = list(range(1, 10))
    grid = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        if solve_grid(grid):
                            return grid
                        else:
                            grid[i][j] = 0
                return None

# Check if a number can be placed in a certain position
def is_valid(grid, row, col, num):
    # Check row
    for j in range(9):
        if grid[row][j] == num:
            return False

    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

# Solve the Sudoku grid using backtracking
def solve_grid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        if solve_grid(grid):
                            return True
                        else:
                            grid[i][j] = 0
                return False
    return True

# Display the Sudoku grid
def display_grid(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(grid[i][j])
            else:
                print(grid[i][j], end=" ")

# Generate a Sudoku puzzle by removing numbers from the complete grid
def generate_puzzle(difficulty):
    puzzle = [row[:] for row in generate_grid()]
    num_cells = 0
    if difficulty == "easy":
        num_cells = random.randint(30, 35)
    elif difficulty == "medium":
        num_cells = random.randint(25, 30)
    elif difficulty == "hard":
        num_cells = random.randint(20, 25)
    else:
        print("Invalid difficulty level!")
        return None

    cells = list(range(81))
    random.shuffle(cells)

    for cell in cells[:num_cells]:
        row = cell // 9
        col = cell % 9
        puzzle[row][col] = 0

    return puzzle

# Get user input for a move
def get_move():
    row = int(input("Enter the row number (1-9): ")) - 1
    col = int(input("Enter the column number (1-9): ")) - 1
    num = int(input("Enter the number (1-9) you want to place: "))
    return (row, col, num)

# Check if the game is complete
def is_complete(grid):
    for row in grid:
        if 0 in row:
            return False
    return True

# Main game loop
def play_game(difficulty):
    puzzle = generate_puzzle(difficulty)
    if puzzle is None:
        return

    print("Welcome to Sudoku!")
    print("Enter row, column, and number (1-9) to place a number in the grid.")
    print("Enter '0' for the number to erase a cell.")
    print()

    while not is_complete(puzzle):
        display_grid(puzzle)
        print()
        row, col, num = get_move()
        if num == 0:
            puzzle[row][col] = 0
        elif is_valid(puzzle, row, col, num):
            puzzle[row][col] = num
        else:
            print("Invalid move!")

    print("Congratulations! You solved the Sudoku puzzle.")
    display_grid(puzzle)

# Start the game
play_game("medium")
