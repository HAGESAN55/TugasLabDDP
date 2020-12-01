print("Soal 1\n")
print("Permainan Batu Gunting Kertas!!")
p1 = input("Pilihan Player 1 = ")
p2 = input("Pilihan Player 2 = ")
if p1 == 'kertas' or p1 == 'Kertas':
  if p2 == 'gunting' or p2 == 'Gunting':
    print("Player 2 menang.")
  elif p2 == 'batu'or p2 == 'Batu':
    print("Player 1 menang.")
  else:
    print("Pertandingan seri.")
elif p1 == 'gunting' or p1 == 'Gunting':
  if p2 == 'kertas' or p2 == 'Kertas':
    print("Player 1 Menang.")
  elif p2 == 'batu' or p2 == 'Batu':
    print("Player 2 Menang.")
  else:
    print("Pertandingan Seri.")
elif p1 == 'batu' or p1 == 'Batu':
  if p2 == 'kertas' or p1 == 'Batu':
    print("Player 2 Menang.")
  elif p2 == 'gunting' or p2 == 'Gunting':
    print("Player 1 Menang.")
  else:
    print("Pertandingan Seri.")
else:
  print("Inputan Error")
