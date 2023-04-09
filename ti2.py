from collections import defaultdict
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        (curr_dist, curr_node) = heapq.heappop(pq)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor, weight in graph[curr_node].items():
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

graph = defaultdict(dict)
n, m = map(int, input().split())
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

for i in range(1, n+1):
    if i == 1:
        print(0)
        continue
    distances = dijkstra(graph, 1)
    if distances[i] == float('inf'):
        print(-1)
    else:
        print(distances[i])