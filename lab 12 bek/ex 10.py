print("\n--- Задание 10 ---")

class SimpleHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Список вложенных списков для цепочек

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        # Добавляем ключ, если его еще нет в цепочке
        if key not in self.table[index]:
            self.table[index].append(key)

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Создаем таблицу размером 5
hash_table = SimpleHashTable(5)
elements_to_add = [10, 20, 25, 7, 12, 17]

for el in elements_to_add:
    hash_table.insert(el)

print("Содержимое хеш-таблицы после вставки элементов [10, 20, 25, 7, 12, 17]:")
hash_table.display()