matrix = list(input())
matrix_2d = []
word = input()
print(matrix)
tmp_list = []
dict = {}
root = len(matrix)**(1/2)
for i in range(len(matrix)): 
    if ((i+1)%root==0 and i!=0):
        tmp_list.append(matrix[i])
        matrix_2d.append(tmp_list)
        tmp_list=[]
    else:
        tmp_list.append(matrix[i])
for i in range(len(matrix_2d)):
    for j in range(i):
        if matrix_2d[i][j] in dict:
            name = str(matrix_2d[i][j])+str(matrix_2d[i][j])
            dict[name]=f"[{i}:{j}]"
        else:
            dict[str(matrix_2d[i][j])]=f"[{i}:{j}]"
print(dict)
        

print(matrix_2d)