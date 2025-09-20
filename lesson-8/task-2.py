N = int(input("Введите N (1..100000): ").strip())
if not (1 <= N <= 100000):
    print("Ошибка: N должно быть в диапазоне 1..100000.")
    raise SystemExit

parts = input("Введите N чисел через пробел (каждый 1..10^9): ").split()
if len(parts) != N:
    print("Ошибка: количество чисел не равно N.")
    raise SystemExit

arr = []
for i, token in enumerate(parts, 1):
    try:
        x = int(token)
    except ValueError:
        print(f"Ошибка: элемент #{i} не является целым числом.")
        raise SystemExit
    if not (1 <= x <= 10**9):
        print(f"Ошибка: элемент #{i} выходит за пределы 1..10^9.")
        raise SystemExit
    arr.append(x)

rotated = [arr[-1]] + arr[:-1] if N > 1 else arr

print("Измененный массив:")
print(*rotated)
