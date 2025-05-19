class ExitError(Exception):
    pass


class IsTitleError(Exception):
    pass


while True:
    # Перевіряємо ім'я для виходу
    try:
        first_name = input("введіть ім'я, або exit для виходу:  ")
        if first_name.lower() == "exit":
            raise ExitError(" Програму завершено, до-побачення")

        if not first_name.istitle():
            raise IsTitleError("Ім`я повинно починатись з великої літери")

    except ExitError as ee:
        print(ee)
        break

    except IsTitleError as ite:
        print(f"Помилка: {ite}")
        print("Спробуйте ще раз.\n")
        continue