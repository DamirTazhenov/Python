#Task D
n = int(input())
ar = []
for i in range(n):
    rows = []
    for j in range(n):
        if (j<n-i-1):
            rows.append('.')
        else:
            rows.append('#')
    if (n%2==1):
        ar.append(rows)
    else:
        rows.reverse()
        ar.append(rows)
    #print()
#print (ar)
for i in range(n):
    for j in range(n):
        print(ar[i][j],end="")
    print()