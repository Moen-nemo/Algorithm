def tile(): #백준 13301 타일 장식물
    n = int(input())
    table = [0] * 81
    table[1] = 1
    table[2] = 1
    for i in range(3, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    print((4 * table[n]) + (2 * table[n - 1]))