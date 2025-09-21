pets = {}

pet_name = input("Введите имя питомца: ").strip()
pet_species = input("Введите вид питомца: ").strip()

while True:
    age_raw = input("Введите возраст питомца (целое число лет): ").strip()
    try:
        pet_age = int(age_raw)
        break
    except ValueError:
        print("Ошибка: возраст должен быть целым числом. Повторите ввод.")

owner_name = input("Введите имя владельца: ").strip()

pets[pet_name] = {
    "Вид питомца": pet_species,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}

def years_word(n: int) -> str:
    n = abs(n)
    if 11 <= (n % 100) <= 14:
        return "лет"
    last = n % 10
    if last == 1:
        return "год"
    if 2 <= last <= 4:
        return "года"
    return "лет"

name_from_dict = next(iter(pets.keys()))
info_from_dict = next(iter(pets.values()))

print(
    f'Это {info_from_dict["Вид питомца"]} по кличке "{name_from_dict}". '
    f'Возраст питомца: {info_from_dict["Возраст питомца"]} '
    f'{years_word(info_from_dict["Возраст питомца"])}. '
    f'Имя владельца: {info_from_dict["Имя владельца"]}'
)

pets = {}

pet_name = input("Введите имя питомца: ").strip()
pet_species = input("Введите вид питомца: ").strip()

while True:
    age_raw = input("Введите возраст питомца (целое число лет): ").strip()
    try:
        pet_age = int(age_raw)
        break
    except ValueError:
        print("Ошибка: возраст должен быть целым числом. Повторите ввод.")

owner_name = input("Введите имя владельца: ").strip()

pets[pet_name] = {
    "Вид питомца": pet_species,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}

def years_word(n: int) -> str:
    n = abs(n)
    if 11 <= (n % 100) <= 14:
        return "лет"
    last = n % 10
    if last == 1:
        return "год"
    if 2 <= last <= 4:
        return "года"
    return "лет"

name_from_dict = next(iter(pets.keys()))
info_from_dict = next(iter(pets.values()))

print(
    f'Это {info_from_dict["Вид питомца"]} по кличке "{name_from_dict}". '
    f'Возраст питомца: {info_from_dict["Возраст питомца"]} '
    f'{years_word(info_from_dict["Возраст питомца"])}. '
    f'Имя владельца: {info_from_dict["Имя владельца"]}'
)
