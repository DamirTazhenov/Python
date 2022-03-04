import json
if __name__ == "__main__":
    with open("LAB4/sample.json","r") as inp:
        #print(inp)
        inp_dict = json.load(inp)
        imdata = inp_dict['imdata']
        #print(imdata)
        #print(json.dumps(imdata, indent = 4, sort_keys=True)) # beatiful output
    print("=======================================================================================")
    print("DN                                                 Description           Speed    MTU") 
    print("-------------------------------------------------- --------------------  ------  ------")
    for item in imdata:
        tmp_dn = item['l1PhysIf']['attributes']['dn']
        tmp_description = item['l1PhysIf']["attributes"]["descr"]
        tmp_speed = item["l1PhysIf"]["attributes"]['speed']
        tmp_mtu = item["l1PhysIf"]["attributes"]['mtu']
        print("{0:50} {1:20} {2:9} {3:4}".format(tmp_dn,tmp_description,tmp_speed,tmp_mtu)) 
        #{0:50} 0 the index of variable 50 is max allowed string