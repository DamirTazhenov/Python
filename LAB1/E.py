inp = list(map(int,input().split()))
flag = 1
for i in range(2,inp[0]):
    if inp[0]%i==0:
     flag = 0
if (inp[0]<501) and (flag==1) and (inp[1]%2==0):
    print ("Good job!")
else:
    print ("Try next time!")
