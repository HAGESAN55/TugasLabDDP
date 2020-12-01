def hitung(a, b, c):
    hasil = 0
    if c == '+':
        hasil = a + b
    elif c == '-':
        hasil = a - b
    elif c == '*':
        hasil = a * b
    else:
        print("Input anda salah")
    print(hasil)
hitung(6, 7, '*')