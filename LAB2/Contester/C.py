n = int(input())
ar = []
for i in range(n):
    rows = []
    for j in range(n):
        #print("i-",i,",j-",j)
        if i==0 and j!=0:
            rows.append(j)
        elif j==0 and i!=0:
            rows.append(i)
        elif i==j:
            rows.append(i*i)
        else:
            rows.append(0)
    ar.append(rows)
    #print()
#print (ar)
for i in range(n):
    for j in range(n):
        print(ar[i][j],end=" ")
    print()