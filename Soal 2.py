n = int(input("Masukkan nilai n: "))

def faktorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

for i in range(n, 0, -1):
    x = faktorial(i)
    print(f"{x} ", end="")
    for j in range(i, 0, -1):
        print(f"{j} ", end="")
    print()