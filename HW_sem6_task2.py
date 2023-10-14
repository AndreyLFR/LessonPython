def is_attacking(q1, q2):
    return True if q1[0] == q2[0] or q1[1] == q2[1] or (abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])) else False

def check_queens(queens):
    for q1 in range(len(queens)):
        for q2 in range(q1 + 1, len(queens)):
            if is_attacking(queens[q1], queens[q2]):
                return True
                break
    return False

queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
print(check_queens(queens))