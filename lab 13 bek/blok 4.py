import time

def get_sum_naive(arr, i, j):
    return sum(arr[i : j + 1])

def get_sum_prefix(prefix_arr, i, j):
    if i == 0:
        return prefix_arr[j]
    return prefix_arr[j] - prefix_arr[i - 1]

# Подготовка данных
data = list(range(1, 1000001)) # 1 млн чисел

# Создаем массив префиксных сумм (тратим память)
start_pre = time.perf_counter()
prefix_sums = [0] * len(data)
prefix_sums[0] = data[0]
for i in range(1, len(data)):
    prefix_sums[i] = prefix_sums[i-1] + data[i]
print(f"Подготовка префиксов заняла: {time.perf_counter() - start_pre:.4f} сек")

# Сравнение запроса
i, j = 100, 900000

start = time.perf_counter()
res_naive = get_sum_naive(data, i, j)
print(f"Обычное суммирование: {res_naive}, Время: {time.perf_counter() - start:.6f} сек")

start = time.perf_counter()
res_pref = get_sum_prefix(prefix_sums, i, j)
print(f"Через префиксы: {res_pref}, Время: {time.perf_counter() - start:.6f} сек")