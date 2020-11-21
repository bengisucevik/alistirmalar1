l=[]
for i in range(1000,10000):
    if str(i)[0] > str(i)[-1]:
        l.append(i)
        i+=1

print(len(l))        
	
