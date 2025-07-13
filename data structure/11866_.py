from collections import deque

n, k = map(int, input().split())
queue = deque()
permutation = []

for i in range(1, n + 1):
    queue.append(str(i)) # join 쓰려고
# [i for i in range(1, n + 1)]
# [list.append(i) for i in range(1, n + 1)]

for i in range(n):
    for _ in range(k - 1):
        queue.append(queue[0])
        queue.popleft()
    permutation.append(queue.popleft())

print(f"<{', '.join(permutation)}>") # join은 리스트 내 str형만 합칠 수 있음
# print("<", end="")
# for i in range(n-1):
#     print(f"{permutation[i]}, ", end="")
# print(f"{permutation[-1]}>")