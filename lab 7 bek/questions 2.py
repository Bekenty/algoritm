count = 10

def change_value():
    global count
    count = 25  # Изменяем глобальную переменную
    
    local_var = 5  # Локальная переменная
    print(f"Внутри функции: count = {count}, local_var = {local_var}")

print(f"До вызова: count = {count}")

change_value()

print(f"После вызова: count = {count}")