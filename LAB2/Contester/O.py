def str_to_int(string):
    if string=="ONE":
        return "1"
    if string=="TWO":
        return "2"
    if string=="THR":
        return "3"
    if string=="FOU":
        return "4"
    if string=="FIV":
        return "5"
    if string=="SIX":
        return "6"
    if string=="SEV":
        return "7"
    if string=="EIG":
        return "8"
    if string=="NIN":
        return "9"
    if string=="ZER":
        return "0"
def int_to_str(integer):
    if integer==1:
        return "ONE"
    if integer==2:
        return "TWO"
    if integer==3:
        return "THR"
    if integer==4:
        return "FOU"
    if integer==5:
        return "FIV"
    if integer==6:
        return "SIX"
    if integer==7:
        return "SEV"
    if integer==8:
        return "EIG"
    if integer==9:
        return "NIN"
    if integer==0:
        return "ZER"
def get_num(strig):
    length = len(strig)
    counter = int(length/3)-1
    i = 1
    result = 0
    while (i<=length):
        tmp = strig[i-1:i+2]
        #print(tmp)
        result += (int(str_to_int(tmp))*(10**(counter)) )
        i+=3
        counter-=1
    return result
def get_str_num(integer):
    #print(integer)
    force_int = int(integer)
    force = 1
    while force_int>9:
        force+=1
        #print(force_int)
        force_int= force_int / 10
    #print (force)
    answer=""
    for i in range(force):
        tmp = int(integer/(10**(force-i-1)))
        #print(tmp)
        integer = int(integer % 10**(force-i-1))
        answer+=str(int_to_str(tmp))
    return answer

numbers = list(map(str,input().split("+")))
print(get_str_num(get_num(numbers[0])+get_num(numbers[1])))
