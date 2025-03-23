tinggi = int(input("Masukkan tinggi matriks: "))
lebar = int(input("Masukkan lebar matriks: "))

angka = 1

for i in range(tinggi):
    for j in range(lebar):
        print(angka, end=" ")
        angka += 1
    print()