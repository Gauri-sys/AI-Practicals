import sys
import heapq

def get_user_grid(title):
    print(f"\n--- Enter {title} ---")
    print("Enter 3 rows of 3 numbers (0-8, space-separated). Use 0 for the blank tile.")

    grid = []
    tiles_seen = set()

    for i in range(3):
        row_input = input(f"Row {i+1}: ").strip().split()

        if len(row_input) != 3:
            print("Error: You must enter exactly 3 numbers per row. Program terminating.")
            sys.exit(1)

        row = []
        for val in row_input:
            if not val.isdigit() or int(val) < 0 or int(val) > 8:
                print(f"Error: Invalid tile '{val}'. Must be an integer 0-8. Program terminating.")
                sys.exit(1)

            num = int(val)
            if num in tiles_seen:
                print(f"Error: Duplicate tile '{num}' detected. Program terminating.")
                sys.exit(1)

            tiles_seen.add(num)
            row.append(num)

        grid.append(tuple(row))

    # Verify exactly 9 tiles were provided (0-8)
    if len(tiles_seen) != 9:
        print("Error: Grid does not contain all unique tiles from 0 to 8. Program terminating.")
        sys.exit(1)

    return tuple(grid)

def map_goal_positions(goal_state):
    positions = {}
    for i in range(3):
        for j in range(3):
            positions[goal_state[i][j]] = (i, j)
    return positions

class PuzzleNode:
    def __init__(self, state, goal_state, goal_positions, parent=None, move="", g=0):
        self.state = state
        self.goal_state = goal_state
        self.goal_positions = goal_positions
        self.parent = parent
        self.move = move
        self.g = g
        self.h = self.calculate_manhattan()
        self.f = self.g + self.h

    def calculate_manhattan(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                tile = self.state[i][j]
                if tile != 0:
                    target_row, target_col = self.goal_positions[tile]
                    distance += abs(target_row - i) + abs(target_col - j)
        return distance

    def __lt__(self, other):
        return self.f < other.f

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_successors(node):
    successors = []
    row, col = get_blank_position(node.state)

    moves = {
        "Up": (-1, 0),
        "Down": (1, 0),
        "Left": (0, -1),
        "Right": (0, 1)
    }

    for move_name, (dr, dc) in moves.items():
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [list(r) for r in node.state]
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
            new_state_tuple = tuple(tuple(r) for r in new_state)

            child_node = PuzzleNode(
                state=new_state_tuple,
                goal_state=node.goal_state,
                goal_positions=node.goal_positions,
                parent=node,
                move=move_name,
                g=node.g + 1
            )
            successors.append(child_node)

    return successors

def print_solution(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    path.reverse()

    print(f"\nOptimal Solution Found in {len(path) - 1} moves!\n")
    for step, n in enumerate(path):
        action = f"Move: {n.move}" if n.move else "Initial State"
        print(f"Step {step} | {action} | f(n)={n.f} [g={n.g}, h={n.h}]")
        for row in n.state:
            print(" " + " ".join(str(val) if val != 0 else "_" for val in row))
        print("-" * 30)

def solve_8_puzzle_a_star(start_state, goal_state):
    goal_positions = map_goal_positions(goal_state)

    start_node = PuzzleNode(start_state, goal_state, goal_positions)

    open_list = []
    heapq.heappush(open_list, start_node)

    visited = set()
    visited.add(start_state)

    print("\nStarting A* Search...")

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            print_solution(current_node)
            return

        for child in generate_successors(current_node):
            if child.state not in visited:
                visited.add(child.state)
                heapq.heappush(open_list, child)

    print("Error: No solution exists for this initial configuration.")

if __name__ == "__main__":
    initial_board = get_user_grid("Initial State")
    target_board = get_user_grid("Target Goal State")

    solve_8_puzzle_a_star(initial_board, target_board)