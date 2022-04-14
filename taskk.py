matrix = list(input())
dict = {}
x,y =0,0
root = len(matrix)**(1/2)
key=[]
for i in range(len(matrix)):
    if ((i+1)%root==0 and i!=0):
        key = (i,matrix[i])
        dict[key]=f"{x}:{y}"
        x+=1
        y=0
    else:
        key = (i,matrix[i])
        dict[key]=f"{x}:{y}"
        y+=1
print(dict)

word = input()
for i in dict:
    if word[0] == i[]:
        base_point = i[]