result = {}
sorted_list = []

while True:
    inp = input()
    list_int = list(map(str,inp.split())) # для сортироки
    if inp=="0":
        break

    inp_int = int(list_int[2]+list_int[1]+list_int[0])
    sorted_list.append(inp_int)
    result.update({inp_int:inp})

sorted_list.sort()
for i in sorted_list:
    print(result.get(i))
