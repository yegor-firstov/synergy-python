def factorial(k: int) -> int:
    if k < 1:
        raise ValueError("Аргумент должен быть натуральным (≥ 1).")
    res = 1
    for i in range(2, k + 1):
        res *= i
    return res

# Ввод
n = int(input("Введите натуральное число n: ").strip())
if n < 1:
    print("Ошибка: n должно быть натуральным (≥ 1).")
    raise SystemExit

# 1) Факториал n
f = factorial(n)
print(f"Факториал числа {n} равен {f}")

# 2) Список факториалов чисел от f до 1: [f!, (f-1)!, ..., 1!]
# Чтобы не считать каждый факториал с нуля, используем связь: (k-1)! = k! / k
seq = []
cur = factorial(f)   # это f!
seq.append(cur)
for k in range(f, 1, -1):
    cur //= k        # теперь cur = (k-1)!
    seq.append(cur)

print("Список факториалов от", f, "до 1 (убывающе):")
print(seq)
