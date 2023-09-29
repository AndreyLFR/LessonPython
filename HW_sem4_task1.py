matrix = [[1, 2, 3], [4, 5,6], [7, 8, 9]]

def transpose(matrix):
    return list(map(list, zip(*matrix)))

transposed_matrix = transpose(matrix=matrix)
print(transposed_matrix)
