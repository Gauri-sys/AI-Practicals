import random
import sys

def get_user_grid():
    """Prompts the user for the 2x2 grid state with strict validation."""
    grid = []
    print("Enter the state of the 2x2 grid (0 for Clean, 1 for Dirty).")
    for i in range(2):
        row = []
        for j in range(2):
            val = input(f"Enter state for tile ({i}, {j}): ").strip()
            if val not in ('0', '1'):
                print(f"Invalid input '{val}'. Expected 0 or 1. Program terminating.")
                sys.exit(1)
            row.append(int(val))
        grid.append(row)
    return grid

def is_environment_clean(grid):
    """Checks if the 2x2 matrix contains any 1s (Dirty)."""
    return all(cell == 0 for row in grid for cell in row)

def display_grid(grid, agent_x, agent_y):
    """Renders the grid cleanly with fixed-width formatting."""
    for i in range(len(grid)):
        row_display = []
        for j in range(len(grid[i])):
            status = "Dirty" if grid[i][j] == 1 else "Clean"
            if i == agent_x and j == agent_y:
                row_display.append(f"[{status} (Agent)]".center(17))
            else:
                row_display.append(f"{status}".center(17))
        print(" | ".join(row_display))
    print("-" * 37)

def reflex_vacuum_agent(grid, start_x, start_y):
    x, y = start_x, start_y
    grid_size = len(grid)
    step = 0

    print("\nInitial Environment State:")
    display_grid(grid, x, y)
    print("\nExecution Log:")

    while not is_environment_clean(grid):
        step += 1

        # 1. Evaluate Current Tile State
        initial_state = "Dirty" if grid[x][y] == 1 else "Clean"
        action_taken = "None"

        # 2. Execute Action if Dirty
        if grid[x][y] == 1:
            action_taken = "Suck"
            grid[x][y] = 0 # Update state

        post_action_state = "Dirty" if grid[x][y] == 1 else "Clean"

        # 3. Determine Valid Boundaries & Next Move
        valid_moves = []
        if x > 0: valid_moves.append(("Up", -1, 0))
        if x < grid_size - 1: valid_moves.append(("Down", 1, 0))
        if y > 0: valid_moves.append(("Left", 0, -1))
        if y < grid_size - 1: valid_moves.append(("Right", 0, 1))

        # Check if environment is completely clean before picking the next move
        if is_environment_clean(grid):
            move_name = "None (Goal Reached)"
            dx, dy = 0, 0
        else:
            move_name, dx, dy = random.choice(valid_moves)

        # Print the consolidated step log
        print(f"Step {step:2} | Coord: ({x},{y}) | State: {initial_state:5} | Action: {action_taken:4} | Post-State: {post_action_state:5} | Next Move: {move_name}")

        # 4. Apply Movement
        x += dx
        y += dy

    print(f"\nMission Accomplished in {step} steps. The 2x2 grid is fully clean.")
    print("Final Environment State:")
    display_grid(grid, x, y)

if __name__ == "__main__":
    room_grid = get_user_grid()
    reflex_vacuum_agent(room_grid, 0, 0)