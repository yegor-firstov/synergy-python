A = int(input("Введите A (целое, A ≤ B): "))
B = int(input("Введите B (целое): "))

start = A if A % 2 == 0 else A + 1
if start > B:
    print()
else:
    evens = range(start, B + 1, 2)
    print(*evens)
