e = 0
fakt=1
n = int(input('büyük bir değer giriniz:'))
for i in range(0,n):
    fakt = fakt*(i+1)
    e = e + (1/fakt)

    
print('e sayısının yaklaşık değeri:',e+1)
