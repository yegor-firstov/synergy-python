import math

X = int(input("Введите натуральное число X: ").strip())
if X <= 0:
    print("Ошибка: X должно быть натуральным (X ≥ 1).")
else:
    n = X
    divisors = 1

    exp = 0
    while n % 2 == 0:
        n //= 2
        exp += 1
    if exp:
        divisors *= (exp + 1)

    p = 3
    while p * p <= n:
        exp = 0
        while n % p == 0:
            n //= p
            exp += 1
        if exp:
            divisors *= (exp + 1)
        p += 2

    if n > 1:
        divisors *= 2

    print(f"Количество делителей числа {X}: {divisors}")
