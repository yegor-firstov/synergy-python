start = int(input("Введите начальное целое число (начало диапазона): ").strip())
end = int(input("Введите конечное целое число (конец диапазона): ").strip())

my_dict = {}
step = 1 if start <= end else -1
for k in range(start, end + step, step):
    my_dict[k] = k ** k

print("Сформированный словарь:")
print(my_dict)
