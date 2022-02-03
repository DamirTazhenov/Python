n = int(input())
for i in range(0,n):
    tmp_word = input()
    if (tmp_word.find("@gmail.com")!=-1):
        print(tmp_word.replace("@gmail.com",""))
    
    
