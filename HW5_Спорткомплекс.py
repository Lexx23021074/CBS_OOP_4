class TrainerNotFoundError(Exception):
    """Власний клас винятку для обробки випадків, коли тренера не знайдено"""
    pass

def show_sports(sports):
    print("\n Перелік видів спорту:")
    for sport in sports:
        print(f"- {sport}")


def show_trainers(trainers):
    print("\n🔹 Команда тренерів:")
    for surname, info in trainers.items():
        print(f"- {info['імʼя']} {surname}, вид спорту: {info['спорт']}")

    search = input("\n Введіть прізвище тренера для пошуку: ").capitalize()
    try:
        if search not in trainers:
            raise TrainerNotFoundError(f"Тренера з прізвищем '{search}' не знайдено.")
        trainer = trainers[search]
        print(f"\n Знайдено: {trainer['імʼя']} {search}, вид спорту: {trainer['спорт']}")
    except TrainerNotFoundError as e:
        print(f" Помилка: {e}")


def show_schedule(schedule):
    print("\n Розклад тренувань:")
    for sport, time in schedule.items():
        print(f"- {sport}: {time}")


def show_prices(prices):
    print("\n Вартість тренувань:")
    for sport, price in prices.items():
        print(f"- {sport}: {price} грн/заняття")

def main():
    # Дані
    sports = ["Футбол", "Баскетбол", "Теніс", "Йога"]

    trainers = {
        "Петренко": {"імʼя": "Іван", "спорт": "Футбол"},
        "Сидоренко": {"імʼя": "Марина", "спорт": "Йога"},
        "Коваль": {"імʼя": "Олег", "спорт": "Баскетбол"},
    }

    schedule = {
        "Футбол": "Пн, Ср, Пт о 18:00",
        "Баскетбол": "Вт, Чт о 17:00",
        "Теніс": "Пн, Ср, Пт о 16:00",
        "Йога": "Щодня о 08:00",
    }

    prices = {
        "Футбол": 150,
        "Баскетбол": 130,
        "Теніс": 180,
        "Йога": 100,
    }

    # Головне меню
    while True:
        print("\n Меню спортивного комплексу:")
        print("1 - Перелік видів спорту")
        print("2 - Команда тренерів (з пошуком)")
        print("3 - Розклад тренувань")
        print("4 - Вартість тренування")
        print("0 - Вихід")

        choice = input("Виберіть пункт меню: ")

        if choice == "1":
            show_sports(sports)
        elif choice == "2":
            show_trainers(trainers)
        elif choice == "3":
            show_schedule(schedule)
        elif choice == "4":
            show_prices(prices)
        elif choice == "0":
            print(" До побачення!")
            break
        else:
            print(" Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()





'''

Створіть програму спортивного комплексу, у якій передбачене меню:
 1 - перелік видів спорту,
 2 - команда тренерів,
 3 - розклад тренувань,
 4 - вартість тренування.1
 Дані зберігати у словниках.
  Також передбачити пошук по прізвищу тренера, яке вводиться з клавіатури у відповідному пункті меню.
Якщо ключ не буде знайдений, створити відповідний клас-Exception, який буде викликатися в обробнику виключень.
'''