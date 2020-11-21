l=[]
for i in range(100,1000,2):
    if str(i)[0] == str(i)[1] :
        l.append(i)
        print(i)
    elif str(i)[0] == str(i)[2]:
            l.append(i)
            print(i)
            
    elif str(i)[1] == str(i)[2]:
                l.append(i)
                print(i)

print(len(l))
