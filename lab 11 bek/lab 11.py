from collections import deque

# создаём граф
graph = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6'],
    '4': ['2'],
    '5': ['2', '6'],
    '6': ['3', '5']
}

# добавим новую вершину
graph['7'] = ['3', '4']
graph['3'].append('7')
graph['4'].append('7')

# функция получения соседей
def neighbors(g, vertex):
    return g.get(vertex, [])

print("Соседи вершины 3:", neighbors(graph, '3'))

# DFS через стек
def dfs(graph, start):
    visited = set()
    stack = [start]

    print("DFS:", end=' ')
    while stack:
        current = stack.pop()

        if current not in visited:
            print(current, end=' ')
            visited.add(current)

            # добавляем соседей в стек
            for n in reversed(graph[current]):
                if n not in visited:
                    stack.append(n)

# BFS через очередь
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("\nBFS:", end=' ')
    while queue:
        current = queue.popleft()

        if current not in visited:
            print(current, end=' ')
            visited.add(current)

            for n in graph[current]:
                if n not in visited:
                    queue.append(n)

# вызовы
dfs(graph, '1')
bfs(graph, '1')