s = input("Введите строку без пробелов: ").strip().lower()
print("yes" if s == s[::-1] else "no")
