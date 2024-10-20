input_data = list(map(int, input().split()))

# n adalah angka pertama
n = input_data[0]

# Sisanya adalah data edge
edges_data = input_data[1:]

edges = {}

# Proses setiap triplet (u, v, w) dari edges_data
for i in range(0, len(edges_data), 3):
    u, v, w = edges_data[i], edges_data[i + 1], edges_data[i + 2]
    if u not in edges:
        edges[u] = []
    edges[u].append((v, w))


def dfs(node, parent):
    max_time = 0
    if node not in edges:
        return 0
    for neighbor, time in edges[node]:
        if neighbor != parent:
            max_time += time + dfs(neighbor, node)
    return max_time


result = dfs(1, -1)
print(result)