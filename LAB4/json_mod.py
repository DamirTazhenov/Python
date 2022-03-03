import json
if __name__ == "__main__":
    with open("LAB4/sample.json","r") as inp:
        #print(inp)
        inp_dict = json.load(inp)
        imdata = inp_dict['imdata']
        print(imdata)
    print("=======================================================================================")
    print("DN                                                 Description           Speed    MTU") 
    print("-------------------------------------------------- --------------------  ------  ------")
    for item in imdata:
        tmp_dn = item['l1PhysIf']['attributes']['dn']
        tmp_description = item['l1PhysIf']["attributes"]["descr"]
        tmp_speed = item["l1PhysIf"]["attributes"]['speed']
        tmp_mtu = item["l1PhysIf"]["attributes"]['mtu']
        print("{} {} {} {}".format(tmp_dn,tmp_description,tmp_speed,tmp_mtu))