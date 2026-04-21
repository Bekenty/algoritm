def sort_by_length(strings):
    return sorted(strings, key=len)

# Пример
print(sort_by_length(["apple", "pie", "banana"]))  # ['pie', 'apple', 'banana']