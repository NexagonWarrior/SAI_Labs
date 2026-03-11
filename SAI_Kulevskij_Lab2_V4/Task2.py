import math


def get_matrix_from_input():
    while True:
        try:
            line = input("Введіть цілі числа через пробіл: ")
            numbers = list(map(int, line.split()))

            if not numbers:
                print("Ви нічого не ввели. Спробуйте ще раз.")
                continue
            n = int(math.sqrt(len(numbers)))

            if n * n != len(numbers):
                print(f"Помилка! Кількість чисел ({len(numbers)}) не дозволяє створити квадратну матрицю n x n.")
                print("Кількість чисел має бути 4, 9, 16, 25 і т.д.")
                continue

            matrix = [numbers[i * n: (i + 1) * n] for i in range(n)]
            return matrix, n

        except ValueError:
            print("Помилка! Вводьте лише цілі числа.")


def is_anti_diagonal_symmetric(matrix, n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
                return False
    return True


matrix, n = get_matrix_from_input()

print("\nВаша матриця:")
for row in matrix:
    print(row)

if is_anti_diagonal_symmetric(matrix, n):
    print("\nМатриця СИМЕТРИЧНА відносно побічної діагоналі.")
else:
    print("\nМатриця НЕ симетрична відносно побічної діагоналі.")