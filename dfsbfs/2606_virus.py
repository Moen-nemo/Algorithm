from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    count = 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                count += 1  # 새로 감염된 컴퓨터 수 증가

    return count

n = int(input())  # 컴퓨터 수
numOfPair = int(input())  # 연결된 쌍의 수

# 그래프 생성
graph = {i: [] for i in range(1, n + 1)}

for _ in range(numOfPair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(graph, 1))
