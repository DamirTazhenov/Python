
reliable = []
def check(passw):
    isLower = False
    isUpper = False
    isDig = False
    for i in passw:
        tmp_ord = ord(i)
        if (isLower==False) and (tmp_ord>96 and tmp_ord<123):
            isLower = True
        if (isUpper==False) and (tmp_ord>64 and tmp_ord<91):
            isUpper = True
        if (isDig==False) and (tmp_ord>47 and tmp_ord<58):
            isDig = True
    if isLower and isUpper and isDig:
        return True
    else:
        return False 


num_password = int(input())

for i in range(num_password):
    tmp = input()
    if check(tmp):
        if tmp not in reliable:
            reliable.append(tmp)

reliable.sort()

print(len(reliable))
for i in reliable:
    print(i)