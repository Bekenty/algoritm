print("\n--- Задание 4 ---")
phone_book = {
    "BEK": "+7-900-111-2233",
    "Damir aga": "+7-900-444-5566",
    "Sasha": "+7-900-777-8899",
    "Diar": "+7-900-000-1122",
    "Amir": "+7-900-333-4455"
}

def find_phone(name):
    return phone_book.get(name, "Контакт не найден")
print(f"Поиск BEK: {find_phone('BEK')}")
print(f"Поиск Damir aga: {find_phone('Damir aga')}")