a = set(map(int, input("Первый список (через пробел): ").split()))
b = set(map(int, input("Второй список (через пробел): ").split()))
print("Количество общих чисел:", len(a & b))
