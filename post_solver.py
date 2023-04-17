import sys


class node():
    def __init__(self, parent, choice: str, list1: str, list2: str) -> None:
        self.parent = parent
        self.list1 = list1
        self.list2 = list2

        self.choices = ""
        if parent and choice:
            self.choices = parent.choices
            self.choices += choice

    # Check if solution
    def is_sol(self):
        # If is root, cant be solution
        if not self.parent:
            return False

        # Check if lengths are equal
        if len(self.list1) != len(self.list2):
            return False

        return True

    def check(self):
        # Checks if all pairs are the same
        for a, b in zip(self.list1, self.list2):
            if a != b:
                return False

        return True

    def __str__(self) -> str:
        return f"({self.list1}, {self.list2}, {str(self.choices)}, {len(self.choices)})"

    def __repr__(self) -> str:
        return self.__str__()


def bfs(A, B):
    # Initialize root node
    initial = node(None, None, "", "")

    # Initializes the fringe
    fringe = [initial]

    while not False:
        # Get node from fringe
        n = fringe.pop(0)

        # Check if solution
        if n.is_sol():
            return n

        # Expand node
        for i, (a, b) in enumerate(zip(A, B)):
            new = node(n, str(i+1), n.list1 + a, n.list2 + b)

            # Check if is worth to expand
            if new.check():
                fringe.append(new)


def parse(filename):
    with open(filename, "r") as f:
        A = f.readline().split(" ")
        A[-1] = A[-1][:-1]  # Removes \n from last item
        B = f.readline().split(" ")
        return A, B


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("ERROR!\n\nUsage: \n post_solver.py <filename.txt>")
        exit(1)

    filename = sys.argv[1]

    print(f"Loading problem from {filename}")
    A, B = parse(filename)
    print(A, B)
    sol = bfs(A, B)
    print(sol)
