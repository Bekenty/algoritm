print("\n--- Задание 2 ---")
numbers = [500, 200, 500, 300, 200, 500]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

for num, count in frequency.items():
    print(f"Число {num} встречается {count} раз(а)")