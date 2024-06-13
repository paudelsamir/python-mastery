import random

# Define the game grid size
GRID_SIZE = 5

# Initialize the game grid with empty spaces
game_grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Place the player on the grid
player_pos = [0, 0]
game_grid[player_pos[0]][player_pos[1]] = 'P'

# Define the exit point
exit_pos = [GRID_SIZE-1, GRID_SIZE-1]
game_grid[exit_pos[0]][exit_pos[1]] = 'E'

# Place some obstacles randomly on the grid
obstacles = [(1, 2), (2, 1), (3, 3)]
for obstacle in obstacles:
    game_grid[obstacle[0]][obstacle[1]] = 'X'

def display_grid():
    for row in game_grid:
        print(' '.join(row))

def move_player(direction):
    global player_pos
    new_pos = player_pos[:]
    if direction == 'W':  # Up
        new_pos[0] -= 1
    elif direction == 'S':  # Down
        new_pos[0] += 1
    elif direction == 'A':  # Left
        new_pos[1] -= 1
    elif direction == 'D':  # Right
        new_pos[1] += 1
    # Check if new position is within the grid and not an obstacle
    if 0 <= new_pos[0] < GRID_SIZE and 0 <= new_pos[1] < GRID_SIZE and game_grid[new_pos[0]][new_pos[1]] != 'X':
        # Update the grid and player position
        game_grid[player_pos[0]][player_pos[1]] = ' '
        player_pos = new_pos
        game_grid[player_pos[0]][player_pos[1]] = 'P'

# Game loop
while player_pos != exit_pos:
    display_grid()
    move = input("Enter move (W/A/S/D): ").upper()
    move_player(move)

print("Congratulations! You've escaped the island!")
