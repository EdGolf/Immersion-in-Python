from Exercise_1 import check_queens_solution, view_queens_solution

true_solution = ((3, 0), (7, 1), (0, 2), (2, 3), (5, 4), (1, 5), (6, 6), (4, 7))
false_solution = ((0, 0), (7, 1), (1, 2), (6, 3), (2, 4), (5, 5), (3, 6), (4, 7))

print(check_queens_solution(true_solution))
view_queens_solution(true_solution)
print()
print(check_queens_solution(false_solution))
view_queens_solution(false_solution)