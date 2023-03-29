Initial_matrix = [[1, 2, 3],
                 [11, 12, 13],
                 [22, 23, 24],
                 [33, 34, 35],
                 [44, 45, 46]]


def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    new_rows_from_columns = zip(*matrix)
    return list(new_rows_from_columns)


def print_matrix(matrix: list[list[int]]):
    for row in matrix:
        for item in row:
            print(f"{item:4}", end="")
        print()


print("Initial matrix")
print_matrix(Initial_matrix)
Transposed_matrix = transpose_matrix(Initial_matrix)
print("\nTransposed matrix")
print_matrix(Transposed_matrix)