import random

# Ввод размеров матрицы
rows = int(input("111"))
cols = int(input("100"))

# Создание двумерного массива
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 20))
    matrix.append(row)

# Вывод матрицы
print("\nМатрица:")
for row in matrix:
    for value in row:
        print(f"{value:4}", end="")
    print()

# Нахождение суммы и максимального элемента
total = 0
maximum = matrix[0][0]

for row in matrix:
    for value in row:
        total += value
        if value > maximum:
            maximum = value

print("\nСумма всех элементов:", total)
print("Максимальный элемент:", maximum)