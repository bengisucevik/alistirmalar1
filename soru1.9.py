l=[]
for i in range(1,10):
    l.append(i)
for i in range(10,100):
    if int(str(i)[0])+int(str(i)[1]) < 9:
        l.append(i)
for i in range(100,1000):
    if int(str(i)[0])+int(str(i)[1])+int(str(i)[2]) < 9:
        l.append(i)

print(*l,sep=' ')
        
        
        
