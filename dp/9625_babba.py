def babba(): #백준 9625 BABBA
    k = int(input())
    table = [0] * 46

    table[1] = 1
    table[2] = 1
    for i in range(3, k + 1):
        table[i] = table[i - 1] + table[i - 2]

    # print(table[k-1], end=' ')
    # print(table[k])
    print(table[k-1], table[k])