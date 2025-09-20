m = int(input("Введите грузоподъёмность лодки m (1..1_000_000): ").strip())
if not (1 <= m <= 10**6):
    print("Ошибка: m должно быть в диапазоне 1..1_000_000.")
    raise SystemExit

n = int(input("Введите количество рыбаков n (1..100): ").strip())
if not (1 <= n <= 100):
    print("Ошибка: n должно быть в диапазоне 1..100.")
    raise SystemExit

weights = []
for i in range(1, n + 1):
    w = int(input(f"Введите вес рыбака #{i} (1..{m}): ").strip())
    if not (1 <= w <= m):
        print(f"Ошибка: вес рыбака #{i} должен быть в диапазоне 1..{m}.")
        raise SystemExit
    weights.append(w)

weights.sort()
i, j = 0, n - 1
boats = 0

while i <= j:
    boats += 1
    if weights[i] + weights[j] <= m:
        i += 1
    j -= 1

print("Минимальное количество лодок:", boats)
