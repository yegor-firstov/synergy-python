species = input("Введите вид питомца: ")
age_str = input("Введите возраст питомца (полных лет): ")
name = input("Введите кличку питомца: ")

age = int(age_str)

if 11 <= age % 100 <= 14:
    years = "лет"
elif age % 10 == 1:
    years = "год"
elif 2 <= age % 10 <= 4:
    years = "года"
else:
    years = "лет"

print(f'Это {species} по кличке "{name}". Возраст: {age} {years}.')