import re
from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()

T = int(input())
for i in range(T):
    p = input()
    n = int(input())
    arr = input()
    arr = re.findall(r"\d+", arr)
    arr = deque(arr)
    rev = 0
    for j in range(len(p)):
        if arr:
            if p[j] == "R":
                rev += 1
            else:
                if rev % 2 != 0:
                    arr.pop()
                else:
                    arr.popleft()
        else: break
    if rev % 2 != 0: arr.reverse()
    if arr:
        arrarr = [k for k in arr]
        print(arrarr)
    else: print("error")