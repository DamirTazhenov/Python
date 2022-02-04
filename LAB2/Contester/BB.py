n = int (input())
inp = list(map(int,input().split()))
inp.sort()
print(inp[-1]*inp[-2])