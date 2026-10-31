class EightQueensCSP:
    def __init__(self):
        self.solutions = []
        self.backtrack_count = 0

    def is_safe(self, board, row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def solve(self, row=0, board=[]):
        if row == 8:
            self.solutions.append(list(board))
            return

        for col in range(8):
            if self.is_safe(board, row, col):
                board.append(col)
                self.solve(row + 1, board)
                board.pop()
            else:
                self.backtrack_count += 1


if __name__ == "__main__":
    csp = EightQueensCSP()
    csp.solve()
    print("="*50)
    print("8-QUEENS CSP EXECUTION SUMMARY")
    print("="*50)
    print(f"Total Valid Solutions Found : {len(csp.solutions)} (Expected: 92)")
    print(f"Total Backtracking Events         : {csp.backtrack_count}")
    print("\nRepresentative Solution 1 Board Configuration:")
    for row in range(8):
        line = ""
        for col in range(8):
            line += " Q " if csp.solutions[0][row] == col else " . "
        print(line)