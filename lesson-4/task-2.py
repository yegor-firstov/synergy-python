n = int(input("Введите пятизначное целое число: "))

units = n % 10
tens = (n // 10) % 10
hundreds = (n // 100) % 10
thousands = (n // 1000) % 10
ten_thousands = (n // 10000) % 10

result = (tens ** units) * hundreds / (ten_thousands - thousands)
print("Результат вычисления:", float(result))