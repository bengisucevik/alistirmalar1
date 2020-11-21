l=[]
li=[]
lis=[]
for i in range(1,1000):
    for n in range(1,1000):
        if i*n == 121212:
            l.append(i-n)
            li.append(i)
            lis.append(n)
a=min(l)
b=min(li)
c=max(lis)
            
print('en küçük fark değeri olan {} için i = {} ve n= {}'.format(a,b,c))

#henüz bitmedi en küçüğü seçmiyor
   

        
