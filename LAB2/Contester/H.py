points = {}
dist_sorted = []

initial = list(map(int,input().split()))

num_points = int(input())
for i in range(num_points):
    inp = list(map(int,input().split()))
    tmp_dist = ((inp[0]-initial[0])**2+(inp[1]-initial[1])**2) ** 0.5
    points.update({tmp_dist:inp})
    dist_sorted.append(tmp_dist)

dist_sorted.sort() # sorted() store unique data

for i in dist_sorted:
    tmp = points[i]
    print(tmp[0],tmp[1])