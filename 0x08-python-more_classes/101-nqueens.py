#!/usr/bin/python3
"""
Challenge of placing N non-attacking queens on an N×N chessboard"""


from sys import argv

if __name__ == "__main__":
    king = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    puzzle = int(argv[1])
    if puzzle < 4:
        print("N must be at least 4")
        exit(1)

    queen = 0
    while queen < puzzle:
        king.append([queen, None])
        queen += 1

    def already_exists(defend_q):
        """Identify whether the given defend_q is already present"""
        for attack_q in range(puzzle):
            if defend_q == king[attack_q][1]:
                return True
        return False

    def reject(attack_q, defend_q):
        """Identify whether the given defend_q is rejected"""
        if (already_exists(defend_q)):
            return False
        queen = 0
        while (queen < attack_q):
            if abs(king[queen][1] - defend_q) == abs(queen - attack_q):
                return False
            queen += 1
        return True

    def clear_a(attack_q):
        """Performs a clearance of the given attack_q position"""
        for queen in range(attack_q, puzzle):
            king[queen][1] = None

    def nqueens(attack_q):
        """Identify the number of queens in the given attack_q position"""
        for defend_q in range(puzzle):
            clear_a(attack_q)
            if reject(attack_q, defend_q):
                king[attack_q][1] = defend_q
                if (attack_q == puzzle - 1):
                    print(king)
                else:
                    nqueens(attack_q + 1)

    nqueens(0)
