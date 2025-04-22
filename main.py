teams = {
    "Manchester United": 50,
    "Manchester City": 45,
    "Liverpool": 40,
    "Chelsea": 35,
    "Arsenal": 30,
    "Tottenham Hotspur": 25,
    "Newcastle United": 20,
    "Aston Villa": 15,
    "Everton": 10
}

# Виведення турнірної таблиці (список всіх команд)
def display_teams():
    sorted_list = sorted(teams.items(), key=lambda x: x[1], reverse=True)
    for team, points in sorted_list:
        print(f"{team}: {points} очок")

# Перегляд команд за алфавітом
def sorted_teams():
    for team in sorted(teams.keys()):
        print(f"{team}: {teams[team]} очок")

# Додавання нової команди
def add_team(name, points):
    teams[name] = points  # Додаємо команду
    print(f"Додано команду {name} з {points} очками.")

# Видалення команди
def remove_team(name):
    if name in teams:
        del teams[name]
        print(f"Команда {name} видалена.")
    else:
        print("Помилка: такої команди немає.")

# Визначення місця команди та списку слабших команд
def find_team_position(name):
    if name not in teams:
        print(f"Помилка: Команда {name} відсутня у списку.")
        return

    sorted_list = sorted(teams.items(), key=lambda x: x[1], reverse=True)  # Сортуємо команди за очками

    position = [team[0] for team in sorted_list].index(name) + 1  # Визначаємо її місце
    weaker_teams = [team[0] for team in sorted_list if team[1] < teams[name]]  # Знаходимо слабші команди

    print(f"Команда {name} зайняла {position}-е місце.")
    print(f"Команди, які набрали менше очок: {', '.join(weaker_teams)}")

# --- Діалог із користувачем ---
while True:
    print("\nМеню:")
    print("1 -> Вивести турнірну таблицю")
    print("2 -> Додати команду")
    print("3 -> Видалити команду")
    print("4 -> Переглянути команди за алфавітом")
    print("5 -> Визначити місце команди")
    print("6 -> Вийти\n")

    choice = input("Ваш вибір: \n")

    if choice == "1":
        display_teams()
    elif choice == "2":
        name = input("Введіть назву команди: ")
        points = int(input("Введіть кількість очок: "))
        add_team(name, points)
    elif choice == "3":
        name = input("Введіть назву команди для видалення: ")
        remove_team(name)
    elif choice == "4":
        sorted_teams()
    elif choice == "5":
        name = input("Введіть назву команди: ")
        find_team_position(name)
    elif choice == "6":
        print("Завершення програми.")
        break
    else:
        print("Помилка: введено некоректний варіант.")