#Task E
n = list(map(int,input().split()))
if(len(n)==1):
    tmp = int(input())
    n.append(tmp)
#arr[i] = x + 2*i
for i in range(n[0]):
    if i==0:
        answ = n[1]
    else:
     tmp = n[1] + (2*i)
     answ = (answ^tmp)
print(answ)