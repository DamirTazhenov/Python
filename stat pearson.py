x = [13, 15, 17, 19, 21, 23, 25, 27, 29 ]
n = [1, 3, 5, 7, 8, 6, 4, 4, 2 ]
n_x = []
x2_n = []
sum_x = 0
sum_n = 0
sum_x_n = 0
sum_x2_n = 0
for i in range(len(n)):
    sum_x+=x[i]
    sum_n+=n[i]
    n_x.append(n[i]*x[i])
    x2_n.append((x[i]**2)*n[i])
    sum_x_n += n[i]*x[i]
    sum_x2_n += (x[i]**2)*n[i]
print(sum_n,sum_x)
print("X*N - ", n_x)
print("x*n - ",sum_x_n)
print("X**2n - ",x2_n)
print("sum -  ",sum_x2_n)
x_av = sum_x/len(x)
sigma = (sum_x2_n/sum_n)-(x_av**2)
dis = sigma**(1/2)
print(x_av,round(sigma,3),round(dis,3))
#step3
zi= []
#z[i] 
for xi in x:
    zi.append(round(((xi-x_av)/dis),2))
print("z[i] - ", zi)
fz = [0.1074, 0.1919, 0.2874, 0.3683, 0.3989, 0.3683, 0.2874, 0.1919, 0.1074]
h=2
nii = []
ni_nii = []
#step4
for i in range(len(fz)):
    nii.append(round((((sum_n*h)/dis)*fz[i]),3))
print("nii - ",nii)
sum_ni_nii = 0
n = [9, 7, 8, 6, 10]
nii=[9.502, 5.965, 6.460, 5.965, 9.502]
for i in range(len(nii)):
    ni_nii.append(round((((n[i]-nii[i])**2)/nii[i]),3))
    sum_ni_nii+=ni_nii[i]
print('ni-nii/nii - ',ni_nii,"\nxhabl**2 - ",sum_ni_nii)
l = 0.05
r = 2
m = 9
k = m - r - 1
xcr_2 = 6