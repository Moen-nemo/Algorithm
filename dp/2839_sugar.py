n = int(input())

arr = [-1]*(n+3)
arr[3] = 1
arr[5] = 1

for i in range(6, n+1):
    if (arr[i-3] != (-1)) and (arr[i-5] != (-1)):
        arr[i] = min(arr[i-3], arr[i-5]) + 1
    if arr[i-3] != (-1):
        arr[i] = arr[i-3] + 1
    if arr[i-5] != (-1):
        arr[i] = arr[i-5] + 1

print(arr[n])