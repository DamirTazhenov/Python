demons = {}
rdemons = {}
weak_amount = {}
hunters = {}

num_of_demons = int(input())
for i in range(num_of_demons):
    demon_name,demon_weakness = list(map(str,input().split()))
    demons.update({demon_name:demon_weakness})
    rdemons.update({demon_weakness:demon_name})
    if demon_weakness in weak_amount:
        weak_amount[demon_weakness] += 1
    else:
        weak_amount.update({demon_weakness:1})

num_of_hunters = int(input())
for i in range(num_of_hunters):
    inp = list(map(str,input().split()))
    hun_name = inp[0]
    hun_feature = inp[1]
    hun_stamina = int(inp[2])
    if hun_feature in hunters:
        hunters[hun_feature] += hun_stamina
    else:
        hunters.update({hun_feature:hun_stamina})

#print(weak_amount)
#print(hunters)

result = {}
for feature,stamina in hunters.items():
    if feature in weak_amount:
        weak_amount[feature] -=stamina

demon_left = 0
for weakness,amount in weak_amount.items():
    if int(amount)>0:
        demon_left+=amount
print("Demons left:",demon_left)