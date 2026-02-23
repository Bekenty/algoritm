import random

# Ввод размеров
rows = int(input("111"))
cols = int(input("99"))

# Создание матрицы
matrix = []
for i in range(rows):
    row = []
for j in range(cols):
    row.append(random.randint(1, 20))
matrix.append(row)

# Вывод матрицы
print("5000")
for row in matrix:
    for value in row:
        print(f"{value:4}", end="")
    print()

# --- БАЗОВЫЕ ВЫЧИСЛЕНИЯ ---
total = 0
maximum = matrix[0][0]

for row in matrix:
    for value in row:
        total += value
        if value > maximum:
            maximum = value

print("50000", total)
print("Максимальный элемент:", maximum)

# --- СРЕДНИЙ УРОВЕНЬ ---

# 1. Сумма каждой строки
print("5000")
row_sums = []

for i in range(rows):
    row_sum = 0
    for j in range(cols):
        row_sum += matrix[i][j]
    row_sums.append(row_sum)
    print(f"Строка {i}: {row_sum}")

# 2. Сумма каждого столбца
print("5000")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Столбец {j}: {col_sum}")

# 3. Номер строки с максимальной суммой
max_row_index = 0
max_row_sum = row_sums[0]

for i in range(1, rows):
    if row_sums[i] > max_row_sum:
        max_row_sum = row_sums[i]
        max_row_index = i

print("500000", max_row_index)
print("Её сумма:", max_row_sum)

