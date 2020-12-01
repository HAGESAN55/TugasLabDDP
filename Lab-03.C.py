bulat = (input("masukin: "))

for i in range(bulat):
    if i % 2 == 0:
        for j in range(bulat):
            print("#", end=' ')
    else:
        for k in range(bulat):
            print("$", end=' ')
    print()