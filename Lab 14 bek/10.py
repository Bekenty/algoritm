def longest_sequence(arr):
    if not arr: return 0
    max_seq = 1
    current_seq = 1
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            current_seq += 1
        else:
            max_seq = max(max_seq, current_seq)
            current_seq = 1
            
    return max(max_seq, current_seq)

# Пример
print(longest_sequence([1, 1, 2, 2, 2, 3, 1]))  # 3 (три двойки подряд)