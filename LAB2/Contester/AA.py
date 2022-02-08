inp = list(map(int,input().split()))
length = len(inp)
i,index = 0,0
max = inp[i]
while(index!=length):
    for i in range(index,inp[index]):
        if inp[i]>max:
            max = inp[i]
            index = i
    print(0)
    break
    