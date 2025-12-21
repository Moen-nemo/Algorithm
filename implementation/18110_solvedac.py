import sys
input = sys.stdin.readline
from decimal import Decimal, ROUND_HALF_UP

numOfComment = int(input())
comment = []
trimmedNumOfComment = int(Decimal((numOfComment * (15 / 100))).to_integral_value(rounding=ROUND_HALF_UP))

if numOfComment == 0: 
    print("0")
    sys.exit()

for i in range(numOfComment):
    comment.append(int(input()))

comment.sort()
trimmedList = comment[trimmedNumOfComment:(numOfComment - trimmedNumOfComment)]
sum = sum(trimmedList)

print(Decimal(sum/len(trimmedList)).to_integral_value(rounding=ROUND_HALF_UP))