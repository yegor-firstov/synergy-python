min_sum = int(input("Минимальная сумма инвестиций X: "))
investor_1 = int(input("У Майкла A: "))
investor_2 = int(input("У Ивана B: "))

if investor_1 >= min_sum and investor_2 >= min_sum:
    print(2)
elif investor_1 >= min_sum:
    print("Mike")
elif investor_2 >= min_sum:
    print("Ivan")
elif investor_1 + investor_2 >= min_sum:
    print(1)
else:
    print(0)
