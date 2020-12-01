bb = eval(input("Masukkan banyak bilangan: "))
jumlah = 0
for k in range(bb):
    bil = eval(input("Masukkan Bilangan: "))
    jumlah = jumlah + bil
print("Rata Rata Bilangan adalah: ", jumlah/bb)