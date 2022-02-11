result = []

inp = input()
result.append(inp[-1])
for i in range(2,len(inp)+1):
    if (len(result)!=0):
        if (result[-1]==']' and inp[-i]=='[') or (result[-1]=='}' and inp[-i]=='{') or (result[-1]==')' and inp[-i] =='('): #обратный принцип
            result.pop(-1)
        else:
            if result[-1]!='}' or result[-1]!="]" or result[-1]!=")":
                result.append(inp[-i])
            else:
                break
    else:
        result.append(inp[-i])
#print(result)
if (len(result)==0):
    print("Yes")
else:
    print("No")
    