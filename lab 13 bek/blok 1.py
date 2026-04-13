import time

def concatenate_with_plus(n):
    res = ""
    for i in range(n):
        res += "a"
    return res

def concatenate_with_join(n):
    res_list = []
    for i in range(n):
        res_list.append("a")
    return "".join(res_list)

n = 500_000

start = time.perf_counter()
concatenate_with_plus(n)
print(f"Обычное сложение (+): {time.perf_counter() - start:.4f} сек")

start = time.perf_counter()
concatenate_with_join(n)
print(f"Использование .join(): {time.perf_counter() - start:.4f} сек")