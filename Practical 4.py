import sys
from collections import deque

def get_disk_count():
    print("\n--- Tower of Hanoi Setup ---")
    try:
        n = int(input("Enter the number of disks: ").strip())
        if n < 1:
            raise ValueError
        return n
    except ValueError:
        sys.exit("Error: Please enter a valid positive integer for the number of disks.")

def print_vertical_board(state, n):
    """
    Renders the Tower of Hanoi vertically using numbers instead of colored blocks.
    """
    print()
    # Iterate from the top row down to the base
    for row in range(n - 1, -1, -1):
        line = ""
        for peg in state:
            if row < len(peg):
                line += f"{peg[row]:^15}"
            else:
                line += f"{'|':^15}"
        print(line)

    print("-" * 45)
    print(f"{'Peg A':^15}{'Peg B':^15}{'Peg C':^15}")
    print()

def generate_valid_moves(state):
    successors = []
    peg_names = ['A', 'B', 'C']

    for src in range(3):
        for dest in range(3):
            if src != dest and state[src]:
                src_top = state[src][-1]
                if not state[dest] or state[dest][-1] > src_top:
                    new_state = [list(peg) for peg in state]
                    disk = new_state[src].pop()
                    new_state[dest].append(disk)

                    new_tuple_state = tuple(tuple(peg) for peg in new_state)
                    move_desc = f"Move Disk {disk} from {peg_names[src]} to {peg_names[dest]}"
                    successors.append((new_tuple_state, move_desc))

    return successors

def solve_hanoi_bfs(num_disks):
    start_peg = tuple(range(num_disks, 0, -1))
    start_state = (start_peg, (), ())
    goal_state = ((), (), start_peg)

    queue = deque([(start_state, [], [start_state])])
    visited = {start_state}

    print(f"\nStarting State Space Search for {num_disks} disks...")

    while queue:
        current_state, path_moves, path_states = queue.popleft()

        if current_state == goal_state:
            print(f"\nOptimal Solution Found in {len(path_moves)} moves!\n")
            print("Initial Configuration:")
            print_vertical_board(path_states[0], num_disks)

            for step, (move, state) in enumerate(zip(path_moves, path_states[1:]), 1):
                print(f"Step {step}: {move}")
                print_vertical_board(state, num_disks)
            return

        for next_state, move_desc in generate_valid_moves(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path_moves + [move_desc], path_states + [next_state]))

if __name__ == "__main__":
    disks = get_disk_count()
    solve_hanoi_bfs(disks)