players = []
pairs = []
while True:
    tmp = int(input())
    if tmp==0:
        break
    players.append(tmp)
length = len(players)
for i in range(int(length/2)):
    pairs.append(players[i]+players[-(i+1)])
if length%2==1:
    pairs.append(players[int(length/2)])
for i in pairs:
    print(i,end=" ")
