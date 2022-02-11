result = []
queue = []

num_operations = int(input())

for i in range(num_operations):
    inp = list(map(str,input().split()))
    if inp[0] == '1':
        queue.append(inp[1])
    else:
        result.append(queue[0])
        queue.pop(0)
for i in result:
    print(i,end=" ")