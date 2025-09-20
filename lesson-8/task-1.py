N = int(input("Введите количество чисел N (1..10000): ").strip())
if not (1 <= N <= 10000):
    print("Ошибка: N должно быть в диапазоне 1..10000.")
    raise SystemExit

arr = []
for i in range(1, N + 1):
    x = int(input(f"Введите число #{i} (|x| ≤ 10^5 = 100000): ").strip())
    if abs(x) > 100000:
        print("Ошибка: модуль числа не должен превышать 100000.")
        raise SystemExit
    arr.append(x)

print("Перевернутый массив:")
print(*reversed(arr))
