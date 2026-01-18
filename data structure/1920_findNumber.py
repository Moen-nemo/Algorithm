import sys
input = sys.stdin.readline

n = int(input())
nArr = list(map(int, input().split()))
m = int(input())
mArr = list(map(int, input().split()))
arrInter = set(nArr) & set(mArr)

for i in mArr:
    if i in arrInter: print("1")
    else: print("0")