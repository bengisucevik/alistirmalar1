l=[]
for i in range(100,1000):
    if int(str(i)[0]) + int(str(i)[1]) == int(str(i)[2]):
        print(i)
        l.append(i)
        i+=1
print(len(l))
        
