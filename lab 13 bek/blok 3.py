import time

# Наивная рекурсия O(2^n)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Итеративный подход O(n)
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Проверка "точки зависания"
n = 35 # Попробуй поставить 40-45, если хочешь подождать подольше

print(f"Вычисляем {n}-е число Фибоначчи...")

start = time.perf_counter()
res_rec = fib_recursive(n)
print(f"Рекурсия: {res_rec}, Время: {time.perf_counter() - start:.4f} сек")

start = time.perf_counter()
res_iter = fib_iterative(n)
print(f"Итерация: {res_iter}, Время: {time.perf_counter() - start:.4f} сек")