def commandFunc(queue, func):
    if func[0] == "push":
        queue.append(func[1])
    elif func[0] == "pop":
        if queue: 
            # print(queue[0])
            # queue = queue[1:]
            print(queue.pop(0))
        else: print("-1")
    elif func[0] == "size":
        print(len(queue))
    elif func[0] == "empty":
        if queue: print("0")
        else: print("1")
    elif func[0] == "front":
        if queue: print(queue[0])
        else: print("-1")
    elif func[0] == "back":
        if queue: print(queue[-1])
        else: print("-1")
    # print(queue)

n = int(input())
queue = []
command = []


for i in range(n):
    command.append(input().split())
    
for i in range(n):
    commandFunc(queue, command[i])
    # print(queue)
