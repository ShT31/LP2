class NQueens:
    def __init__(self, size):
        self.gsize = size
        self.gpos = [-1] * size

    def isSafe(self, row, col):
        for i in range(row):
            if self.gpos[i] == col or abs(self.gpos[i] - col) == abs(i - row):
                return False
        return True

    def btrack(self, row):
        if row == self.gsize:
            self.display()
            return True
        for col in range(self.gsize):
            if self.isSafe(row, col):
                self.gpos[row] = col
                if self.btrack(row + 1):
                    return True
                self.gpos[row] = -1
        return False

    def display(self):
        print("Solution:")
        for i in range(self.gsize):
            for j in range(self.gsize):
                if self.gpos[i] == j:
                    print("Q ", end="")
                else:
                    print(". ", end="")
            print()
        print()

    def branchbound(self, row):
        if row == self.gsize:
            self.display()
            return
        for col in range(self.gsize):
            if self.isSafe(row, col):
                self.gpos[row] = col
                self.branchbound(row + 1)


def main():
    size = int(input("Enter the size of the chessboard (grid size): "))
    q1 = NQueens(size)
    q2 = NQueens(size)
    print("\nBacktracking Solution:")
    if not q1.btrack(0):
        print("No solution exists.\n")
    print("\nBranch and Bound Solution:")
    q2.branchbound(0)


if __name__ == "__main__":
    main()
