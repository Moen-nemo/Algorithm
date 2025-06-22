def fiboLoop(N):
    if N == 0:
        return 0
    if abs(N) < 2:
        return 1
    Arr = [0] * (abs(N)+1)
    Arr[0] = 0
    Arr[1] = 1
    for i in range(2, abs(N)+1):
        Arr[i] = (Arr[i-1] + Arr[i-2]) % 1000000000
    return Arr[abs(N)]

n = int(input()) # 절댓값이 1,000,000 이하

result = fiboLoop(n)

if n == 0:
    print('0')
elif (n < 0) and (n % 2 == 0):
    print('-1')
else:
    print('1')
        
print(result)