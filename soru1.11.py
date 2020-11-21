l=[]
for x in range(1,125):#sayı en çok 125 olabilir
    if 125-(125//x * x) == 200 -(200//x * x) == 350 -(350//x * x):
        l.append(x)

print(max(l))
    
