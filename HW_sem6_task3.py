import random as r

def is_attacking(q1, q2):
    return True if q1[0] == q2[0] or q1[1] == q2[1] or (abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])) else False

def check_queens(queens):
    for q1 in range(len(queens)):
        for q2 in range(q1 + 1, len(queens)):
            if is_attacking(queens[q1], queens[q2]):
                return False
                break
    return True

def generate_boards():
    while True:
        queens = [(r.randint(1, 8), r.randint(1, 8)) for i in range(4)]
        if check_queens(queens):
            board_list = queens
            return board_list
            break


print(generate_boards())




