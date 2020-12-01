def hitung_kesamaan(kata1='', kata2=''):
    a = len(kata1)
    b = len(kata2)
    hasil = 0
    if (a > b):
        for i in range(b):
            per = kata1[i] == kata2[i]
            if per == True:
                hasil = hasil + 1
    else:
        for i in range(a):
            per = kata1[i] == kata2[i]
            if per == True:
                hasil = hasil + 1
    print(hasil)


hitung_kesamaan('apel', 'nanas')