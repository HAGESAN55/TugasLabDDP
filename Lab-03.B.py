print("Toko Buku Bekas!!")
b = eval(input("Berapa banyak buku yang dibeli: "))
if b > 50:
  print("Harga yang harus dibayar Rp.", b * 10000)
elif b >= 26:
    print("Harga yang harus dibayar Rp.", b * 15000)
elif b >= 11:
    print("Harga yang harus dibayar Rp.", b * 18000)
else:
    print("Harga yang harus dibayar Rp.", b * 20000)