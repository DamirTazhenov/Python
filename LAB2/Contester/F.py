#task FFFF
n= int(input())
dicti = {}
rdicti = {}
values = []
for i in range(n):
    tmp_1,tmp_2 = input().split()
    if tmp_1 in dicti: # if the same key is existed we just adding money to the balance else creating new record key:value
        tmp_2_2 = int(dicti.get(tmp_1)) + int(tmp_2)#getting existing money and sum new value
        dicti.update({tmp_1:tmp_2_2})
    else:
        dicti.update({tmp_1:tmp_2})
#print (sorted(dicti))
for x, y in dicti.items():
    rdicti.update({y:x})
list_rdicti = sorted(rdicti)
max = int(list_rdicti[-1])
for i in list_rdicti:
    if max!=int(i):
        print(rdicti.get(i),"has to recieve", max - int(i),"tenge")
    else:
        print(rdicti.get(i),"is lucky!")
