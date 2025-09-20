N = int(input("Введите N (1..100000): ").strip())
if not (1 <= N <= 100000):
    print("Ошибка: N должно быть в диапазоне 1..100000.")
    raise SystemExit

parts = input(f"Введите {N} целых чисел через пробел (|Ai| ≤ 2*10^9): ").split()
if len(parts) != N:
    print("Ошибка: количество чисел не равно N.")
    raise SystemExit

nums = []
for i, tok in enumerate(parts, 1):
    try:
        x = int(tok)
    except ValueError:
        print(f"Ошибка: элемент #{i} не является целым числом.")
        raise SystemExit
    if abs(x) > 2_000_000_000:
        print(f"Ошибка: |элемент #{i}| превышает 2*10^9.")
        raise SystemExit
    nums.append(x)

print("Количество различных чисел:", len(set(nums)))