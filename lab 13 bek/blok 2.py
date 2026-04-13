def logarithmic_demo(n):
    steps = 0
    i = 1
    print(f"Запуск для n = {n}:")
    while i < n:
        print(f"Шаг {steps + 1}: i = {i}")
        i *= 2
        steps += 1
    return steps

n_value = 100
total_steps = logarithmic_demo(n_value)
print(f"\nИтого шагов: {total_steps}")
print(f"Математическое обоснование: log2({n_value}) ≈ 6.64. Наш результат: {total_steps}")