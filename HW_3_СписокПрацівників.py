class Employees:
    def __init__(self, first_name,last_name,department,s_year):
        self.first_name=first_name
        self.last_name=last_name
        self.department=department
        self.s_year=s_year
    def __str__(self):
        return f"{self.first_name} {self.last_name} відділ {self.department} Рік прийняття {self.s_year}"

def main():
    employees = [] # ✅ Список для збереження працівників

    print(" програма Employees, для вводу списку працівників, щоб закінчити наберіть exit замість імені")

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

        try:
            last_name  = input("Введіть фамілію ")
            if not last_name.istitle():
                raise IsTitleError("прізвище повинно починатись з великої літери")
        except IsTitleError as ite:
            print(f"Помилка: {ite}")
            print("Спробуйте ще раз.\n")
            continue
        # --- Ввід департаменту ---
        department = input(" Введіть назву департаменту")

        # --- Ввід року ---
        while True:
            year = input("Введіть рік прийому на роботу:  ")
            try:
                # Перевірка, що введене - це число
                if not year.isdigit(): # Перевірка чи це число
                    raise AttributeError("Рік повинен бути цілим числом")

                # Конвертуємо рядок у число
                s_year = int(year)

                if not (1970 <= s_year <= 2025):
                    raise AttributeError("Рік початку роботи має бути між 1970 і 2025")

                if len(year) != 4:
                    raise AttributeError("Рік має складається з 4-х чисел")

                break

            except AttributeError as ae:
                print(f"Помилка: {ae}")
                print("Введіть коректний рік")

        # --- Додаємо об'єкт до списку ---

        employee = Employees(first_name, last_name, department, s_year)
        employees.append(employee)
    # ----------фільтр по цьогорічно прийнятих

    year_f = input("Введіть рік щоб показати працівників, прийнятих після нього:  ")
    try:
        # Перевірка, що введене - це число
        if not year_f.isdigit():
            raise AttributeError("Рік повинен бути цілим числом")

        # Конвертуємо рядок у число
        filter_year = int(year_f)

        if not (1970 <= filter_year <= 2025):
            raise AttributeError(f"Рік  має бути між 1970 і {filter_year}")

        if len(year_f) != 4:
            raise AttributeError("Рік має складається з 4-х чисел")
        found=False
        for emp in employees:
            if emp.s_year >filter_year:
                print(emp)
                found = True
        if not found:
            print("Немає такких працівників")
    except AttributeError as ae:
        print(f"Помилка: {ae}")
        print("Введіть коректний рік")

if __name__ == "__main__":
        main()
'''
Опишіть клас співробітника,
який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи.
Конструктор має генерувати виняток,  якщо вказано неправильні дані.
Введіть список працівників із клавіатури.
Виведіть усіх співробітників, які були прийняті після цього року.
'''