def is_prime(bilangan):
    if bilangan < 2:
        return False
    for i in range(2, int(bilangan ** 0.5) + 1):
        if bilangan % i == 0:
            return False
    return True

n = int(input("Masukkan nilai n: "))

for i in range(n, 1, -1):
    if is_prime(i):
        print(f"Bilangan prima terdekat < {n} adalah {i}")
        break