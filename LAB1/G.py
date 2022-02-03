word = input()
count = 0
for i in range(0,len(word)):
    bit = int(word[i])
    count+= bit*2**(len(word)-1-i)
print (count)
