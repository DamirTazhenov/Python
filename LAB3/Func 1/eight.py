def spy_game(nums = []):
    complete = ""
    for i in nums:
        if len(complete)!=3:
            if len(complete)==2 and i==7:
                complete +=str(i)
                #print(complete)
            elif len(complete)<2 and i==0:
                complete += str(i)
                #print(complete)
        else:
            return True
    else:
        if len(complete)==3:
            return True
        else:
            return False
if __name__ == "__main__":
    inp = list(map(int,input().split()))
    spy_game(inp)
            