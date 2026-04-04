import sys
import heapq
input = sys.stdin.readline

n = int(input())
heapArr = []

for _ in range(n):
    temp = int(input())
    if temp == 0:
        if heapArr: #안비었음
            print(-heapq.heappop(heapArr))
        else: # 비었음
            print("0")
    else: # 0 x
        heapq.heappush(heapArr, -temp)