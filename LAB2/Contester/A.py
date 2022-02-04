inp = list(map(int,input().split()))
if inp[0]!=0:
    for i in range(1,len(inp)):
     if (inp[i]==0) and (inp[i-1]<2):
         print(0)
         break
    else:
        print(1)