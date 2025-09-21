import collections

pets = {}

def get_suffix(age: int) -> str:
    """Вернуть корректную форму слова 'год' для возраста."""
    n = abs(int(age))
    if 11 <= (n % 100) <= 14:
        return "лет"
    last = n % 10
    if last == 1:
        return "год"
    if 2 <= last <= 4:
        return "года"
    return "лет"

def get_pet(ID: int):
    """Вернуть запись питомца по ID или False, если нет такого ID.
    Возвращаемый объект имеет вид {<имя>: { 'Вид питомца': ..., 'Возраст питомца': ..., 'Имя владельца': ... }}"""
    return pets[ID] if ID in pets.keys() else False

def format_pet_record(record: dict) -> str:
    """Сформировать человекочитаемую строку описания одной записи {name: info}."""
    name = next(iter(record.keys()))
    info = next(iter(record.values()))
    species = info["Вид питомца"]
    age = info["Возраст питомца"]
    owner = info["Имя владельца"]
    return f'Это {species} по кличке "{name}". Возраст питомца: {age} {get_suffix(age)}. Имя владельца: {owner}'

def pets_list():
    """Вывести весь список питомцев (ID + описание)."""
    if not pets:
        print("Список пуст.")
        return
    for ID in pets:
        line = format_pet_record(pets[ID])
        print(f"{ID}: {line}")

def read():
    """Показать запись по ID."""
    ID_raw = input("Введите ID питомца для просмотра: ").strip()
    if not ID_raw.isdigit():
        print("Ошибка: ID должен быть положительным целым числом.")
        return
    ID = int(ID_raw)
    record = get_pet(ID)
    if not record:
        print("Питомец с таким ID не найден.")
        return
    print(format_pet_record(record))

def create():
    """Создать новую запись с автоинкрементом ID (последний ключ + 1)."""
    name = input("Введите кличку питомца: ").strip()
    if not name:
        print("Ошибка: кличка не может быть пустой.")
        return
    species = input("Введите вид питомца: ").strip()
    if not species:
        print("Ошибка: вид питомца не может быть пустым.")
        return

    age_raw = input("Введите возраст питомца (целое число лет): ").strip()
    if not (age_raw.lstrip("-").isdigit()):
        print("Ошибка: возраст должен быть целым числом.")
        return
    age = int(age_raw)

    owner = input("Введите имя владельца: ").strip()
    if not owner:
        print("Ошибка: имя владельца не может быть пустым.")
        return

    if pets:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1
    else:
        new_id = 1

    pets[new_id] = {
        name: {
            "Вид питомца": species,
            "Возраст питомца": age,
            "Имя владельца": owner,
        }
    }
    print(f"Создана запись с ID={new_id}.")
    print(format_pet_record(pets[new_id]))

def update():
    """Обновить поля записи по ID. Пустой ввод — оставить без изменений."""
    ID_raw = input("Введите ID питомца для обновления: ").strip()
    if not ID_raw.isdigit():
        print("Ошибка: ID должен быть положительным целым числом.")
        return
    ID = int(ID_raw)
    record = get_pet(ID)
    if not record:
        print("Питомец с таким ID не найден.")
        return

    old_name = next(iter(record.keys()))
    info = next(iter(record.values()))
    print("Текущая запись:")
    print(format_pet_record(record))

    new_name = input(f'Новая кличка (Enter — оставить "{old_name}"): ').strip()
    if not new_name:
        new_name = old_name

    new_species = input(f'Новый вид (Enter — оставить "{info["Вид питомца"]}"): ').strip()
    if not new_species:
        new_species = info["Вид питомца"]

    age_in = input(f'Новый возраст (целое, Enter — оставить {info["Возраст питомца"]}): ').strip()
    if age_in:
        if not (age_in.lstrip("-").isdigit()):
            print("Ошибка: возраст должен быть целым числом.")
            return
        new_age = int(age_in)
    else:
        new_age = info["Возраст питомца"]

    new_owner = input(f'Новый владелец (Enter — оставить "{info["Имя владельца"]}"): ').strip()
    if not new_owner:
        new_owner = info["Имя владельца"]

    new_info = {
        "Вид питомца": new_species,
        "Возраст питомца": new_age,
        "Имя владельца": new_owner,
    }
    pets[ID] = {new_name: new_info}
    print("Запись обновлена.")
    print(format_pet_record(pets[ID]))

def delete():
    """Удалить запись по ID (без try/except — через проверку наличия ключа)."""
    ID_raw = input("Введите ID питомца для удаления: ").strip()
    if not ID_raw.isdigit():
        print("Ошибка: ID должен быть положительным целым числом.")
        return
    ID = int(ID_raw)
    if ID not in pets:
        print("Питомец с таким ID не найден.")
        return

    print("Удаляем запись:")
    print(format_pet_record(pets[ID]))
    confirm = input("Подтвердите удаление (y/n): ").strip().lower()
    if confirm == "y":
        del pets[ID]
        print("Запись удалена.")
    else:
        print("Удаление отменено.")

def main():
    print("Ветклиника: команды create/read/update/delete/list/stop")
    while True:
        command = input("Введите команду: ").strip().lower()
        if command == "stop":
            print("Выход.")
            break
        elif command == "create":
            create()
        elif command == "read":
            read()
        elif command == "update":
            update()
        elif command == "delete":
            delete()
        elif command == "list":
            pets_list()
        else:
            print("Неизвестная команда. Доступно: create, read, update, delete, list, stop")

if __name__ == "__main__":
    main()
