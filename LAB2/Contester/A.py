inp = list(map(int,input().split()))
length = len(inp)
non_zero_index = 0
if inp[0]!=0:
    for i in range(1,length):
     print(inp[i])
     if (inp[i]!=0) and (inp[non_zero_index]-i<inp[i]):
         non_zero_index=i
     if (inp[i]==0) and (inp[non_zero_index]<=i-non_zero_index) and length-1!=i:
         print(0)
         break
    else:
        print(1)