def stone3():
    n = int(input())
    arr = [False] * (n + 2)
    arr[2] = True
    for i in range(5, n + 1):
        if (arr[i-1] == True) or (arr[i-3] == True) or (arr[i-4] == True):
            arr[i] = False
        else: arr[i] = True
    if arr[n] == False:
        print("SK")
    else: print("CY")