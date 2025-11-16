import sys
from math import log10 # int(log10(n))

input = sys.stdin.readline

n = int(input())
result = 0

for i in range(int(log10(n))):
    result += (i + 1) * 9 * (10 ** i)

result += (n - 10 ** int(log10(n)) + 1) * (int(log10(n)) + 1)

print(result)


# if lenn == 1:
#     print(intn)
# elif lenn == 2:
#     print((intn - 9) * 2 + 9)
# elif lenn == 3:
#     print((intn - 99) * 3 + 189)
# elif lenn == 4:
#     pass
# elif lenn == 5:
#     pass
# elif lenn == 6:
#     pass
# elif lenn == 7:
#     pass
# elif lenn == 8:
#     pass
# else:
#     pass
"""
102 -> 198
3*3 + 90*2 + 9*1

34
25*2 + 9*1

1   9           9
2   90          180
3   900         2700
4   9000        36000
5   90000       450000 
6   900000      5400000
7   9000000     63000000
8   90000000    720000000
9

"""