seri_toplamı=0

n=int(input("seri eleman sayısını giriniz n:"))

for i in range(1,n):
    seri_toplamı=seri_toplamı+(1/i ** 2)
    pi=(seri_toplamı * 6) ** 0.5


#print(seri_toplamı)
print("pi'nin yaklaşık değeri:",pi)
#print(n)
