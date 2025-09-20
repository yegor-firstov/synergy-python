N = int(input("Сколько чисел будет? N: "))
zeros = 0
for _ in range(N):
    if int(input("Введите число: ")) == 0:
        zeros += 1
print("Количество нулей:", zeros)
