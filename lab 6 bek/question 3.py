import random

SIZE = 4

# Создание поля 4x4
def create_field():
    field = []
    for i in range(SIZE):
        row = []
        for j in range(SIZE):
            # Заполняем случайными числами от 0 до 9
            row.append(random.randint(0, 9))
        field.append(row)
    return field

# Красивый вывод поля
def print_field(field):
    for row in field:
        for value in row:
            print(f"{value:4}", end="")
        print()
    print()

# Сдвиг строки вправо (все нули уходят влево)
def shift_right(row):
    non_zero = []
    
    # Собираем ненулевые элементы
    for value in row:
        if value != 0:
            non_zero.append(value)
    
    # Добавляем нужное количество нулей слева
    zeros_count = SIZE - len(non_zero)
    return [0] * zeros_count + non_zero


# -------------------------------
# Основная программа
# -------------------------------

field = create_field()

print("Поле до сдвига:")
print_field(field)

# Сдвигаем каждую строку вправо
for i in range(SIZE):
    field[i] = shift_right(field[i])

print("Поле после сдвига вправо:")
print_field(field)