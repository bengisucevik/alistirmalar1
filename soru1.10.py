l=[]
for i in range(10000,100000):
    if str(i)[0:2] == str(i)[3::]:
        l.append(i)
print(len(l))
    
