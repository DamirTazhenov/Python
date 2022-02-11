#task FFFF
n= int(input())
dicti = {}
rdicti = {}
values = []
sorted_names = []
for i in range(n):
    tmp_1,tmp_2 = input().split()
    if tmp_1 in dicti: # if the same key is existed we just adding money to the balance else creating new record key:value
        tmp_2_2 = int(dicti.get(tmp_1)) + int(tmp_2)#getting existing money and sum new value
        dicti[tmp_1] = tmp_2_2
    else:
        dicti.update({tmp_1:int(tmp_2)})
#print (dicti)
sorted_names = sorted(dicti)
max = 0
for x, y in dicti.items():
    rdicti.update({y:x})
    tmp_int_y = int(y)
    values.append(int(y))
    if max<tmp_int_y:
        max = tmp_int_y

for i in sorted_names:
    if max!=int(dicti.get(i)):
        print(i,"has to receive", max - int(dicti.get(i)),"tenge")
    else:
        print(i,"is lucky!")
