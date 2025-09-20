line = input("Введите последовательность чисел через пробел: ").strip()
seen = set()
for token in line.split():
    x = int(token)
    if x in seen:
        print("YES")
    else:
        print("NO")
        seen.add(x)