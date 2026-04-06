print("\n--- Задание 3 ---")
text = "algorithm"
char_frequency = {}
for char in text:
    char_frequency[char] = char_frequency.get(char, 0) + 1

for char, count in char_frequency.items():
    print(f"Символ '{char}' встречается {count} раз(а)")