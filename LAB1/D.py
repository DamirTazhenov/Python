def afterPoint(num, digits = 0):
    return (f"{num:.{digits}f}")

n = int(input())
z = input()
if (z == 'k'):
    c = input()
    print(afterPoint(n/1024,c))
else:
    print(n*1024)
