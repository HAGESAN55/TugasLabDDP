#while True:
#    nama = input("Masukkan Nama: ")
#    s = nama
#    var2 = len(s)
#    #if  len(nama) < 8:
#    #    print("Rules 1")
#    if 'YYY' or 'yyy' not in nama:
#       print('Rules 2')
#    else:
#        print("Inputan Berhasil")
#        break
# Tuliskan program untuk Soal 2 di bawah ini
# while True:
#   text = input("Masukkan sebuah teks : ")
#   jumlahtext = len(text)

#   if (jumlahtext > 8 
#   and (text.endswith("YYY") or text.endswith("yyy")) 
#   and (text.startswith('NF') or text.startswith('nf') or text.startswith('Nf') or text.startswith('nF'))
#   and (text.isnumeric() == text.isalpha )):
#     print("Teks valid, Selamat Datang.")
#     break
#   else:
#     print("Teks tidak valid.")
while True:
    txt = input("Masukan String : ")
    if len(txt) >= 8 and txt.isnumeric() == txt.isalpha() and (txt.endswith("YYY") or txt.endswith("yyy")) and ("nf" in txt.lower()):
      print("Text Valid, Program berhenti")
      break
    else:
      print("Text Invalid")