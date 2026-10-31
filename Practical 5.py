from collections import deque


class BFSMazeSolver:
    def __init__(self):
        # Default 5x5 maze: 'S' = Start, 'G' = Goal, 0 = Open, 1 = Wall
        self.maze = [
            ['S', 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 0, 'G']
        ]
        self.start = (0, 0)
        self.goal = (4, 4)

    def display_menu(self):
        print("\n============================================================")
        print("        MAZE SOLVING USING BREADTH-FIRST SEARCH (BFS)")
        print("============================================================")
        print("MAIN MENU:")
        print(" 1. View Current Maze Grid")
        print(" 2. Enter Custom Maze Dimensions & Obstacles")
        print(" 3. Run BFS Shortest Path Solver")
        print(" 4. Exit")
        print("------------------------------------------------------------")

    def display_maze(self, path=None):
        path_set = set(path) if path else set()
        print("\n--- Maze Grid Representation ---")
        print("Legend: [S] = Start, [G] = Goal, [.] = Open, [#] = Wall, [*] = Path")
        print("------------------------------------------------------------")

        for r in range(len(self.maze)):
            row_str = ""
            for c in range(len(self.maze[0])):
                pos = (r, c)
                if pos == self.start:
                    row_str += " S "
                elif pos == self.goal:
                    row_str += " G "
                elif pos in path_set:
                    row_str += " * "
                elif self.maze[r][c] == 1:
                    row_str += " # "
                else:
                    row_str += " . "
            print(row_str)

        print("------------------------------------------------------------")

    def customize_maze(self):
        print("\n--- Custom Maze Setup ---")
        try:
            rows = int(input("Enter number of rows (e.g., 5): "))
            cols = int(input("Enter number of columns (e.g., 5): "))

            # Initialize open maze
            self.maze = [[0 for _ in range(cols)] for _ in range(rows)]

            # Set Start and Goal
            sr, sc = map(int, input("Enter Start coordinates (row col, 0-indexed, e.g., 0 0): ").split())
            gr, gc = map(int, input("Enter Goal coordinates (row col, 0-indexed, e.g., 4 4): ").split())

            self.start = (sr, sc)
            self.goal = (gr, gc)
            self.maze[sr][sc] = 'S'
            self.maze[gr][gc] = 'G'

            walls = int(input("Enter total number of wall obstacles: "))
            print("Enter wall coordinates (row col):")
            for _ in range(walls):
                wr, wc = map(int, input("Wall coord: ").split())
                if (wr, wc) != self.start and (wr, wc) != self.goal:
                    self.maze[wr][wc] = 1

            print("\n[SUCCESS] Custom maze configured successfully!")
            self.display_maze()
        except ValueError:
            print("[ERROR] Invalid input format. Please enter numeric values.")

    def solve_bfs(self):
        rows, cols = len(self.maze), len(self.maze[0])
        queue = deque([(self.start, [self.start])])
        visited = {self.start}
        step = 1

        print("\n" + "="*70)
        print("BFS LEVEL-BY-LEVEL EXPLORATION TRACE")
        print("="*70)

        while queue:
            (r, c), path = queue.popleft()
            print(f"Step {step} | Expanding Cell: ({r}, {c}) | Queue Size: {len(queue)}")

            if (r, c) == self.goal:
                print("="*70)
                print(f"[SUCCESS] Goal {self.goal} reached from Start {self.start}!")
                print(f"Shortest Path Length: {len(path)-1} steps")
                print(f"Calculated Optimal Path: {path}")
                print("="*70)
                self.display_maze(path)
                return path

            # Explore 4-directional neighbors (Up, Down, Left, Right)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Check if it's not a wall and not visited
                    if self.maze[nr][nc] != 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append(((nr, nc), path + [(nr, nc)]))
            step += 1

        print("\n[FAILURE] No path exists from Start to Goal (Goal is blocked by walls).")
        return None

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter Choice (1-4): ").strip()

            if choice == '1':
                self.display_maze()
            elif choice == '2':
                self.customize_maze()
            elif choice == '3':
                self.solve_bfs()
            elif choice == '4':
                print("\nExiting BFS Maze Solver. Goodbye!")
                break
            else:
                print("[ERROR] Invalid choice! Please select an option between 1 and 4.")

            input("\nPress Enter to return to the Main Menu...")


if __name__ == "__main__":
    solver = BFSMazeSolver()
    solver.run()