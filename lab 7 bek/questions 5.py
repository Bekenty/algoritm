def max_element(arr, index=0):
    # Базовый случай: дошли до последнего элемента
    if index == len(arr) - 1:
        return arr[index]
    print(f"Максимум в [3, 8, 1, 12, 5]: {max_element([3, 8, 1, 12, 5])}")