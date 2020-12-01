def cetak_nama(nama=''):
    if (nama == ''):
        print("Tidak ada nama yang dicetak")
    else:
        i = 1
        while i <= len(nama):
            print(nama[:i])
            i = i + 1
        print(nama+'!')

cetak_nama('Bujang')

# def test():
#   print("Hasil cetak_nama('Mawar'):")
#   cetak_nama("Mawar")
#   print()
#   print("Hasil cetak_nama(''):")
#   cetak_nama("")
#   print()
#   r = hitung_kesamaan('python', 'path')
#   print(f"hitung_kesamaan('python', 'path') = {r} \t(solusi: 3)")
#   r = hitung_kesamaan('masak', 'cuci')
#   print(f"hitung_kesamaan('masak', 'cuci') = {r} \t(solusi: 0)")
#   r = hitung_kesamaan('python', '')
#   print(f"hitung_kesamaan('python', '') = {r} \t\t(solusi: 0)")
#   print()
#   r = hitung(4, 8)
#   print(f'hitung(4, 8) = {r} \t\t(solusi: 12)')
#   r = hitung(4, 8, '-')
#   print(f"hitung(4, 8, '-') = {r} \t(solusi: -4)")
#   r = hitung(4, 8, '*')
#   print(f"hitung(4, 8, '*') = {r} \t(solusi: 32)")

# if __name__ == '__main__':
#   test()
# #print(end='!')