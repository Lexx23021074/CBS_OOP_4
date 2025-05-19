'''
Напишіть програму-калькулятор, яка підтримує такі операції:
додавання, віднімання, множення, ділення та піднесення до ступеня.
 Програма має видавати повідомлення про помилку та продовжувати роботу
 під час введення некоректних даних,
діленні на нуль та зведенні нуля в негативний степінь.
'''


class Calculator:
    def calculate(self,number_1,number_2):
        pass

class Adder (Calculator):
    def calculate(self,number_1,number_2):
        return number_1+number_2

class Subtractor (Calculator):
    def calculate(self,number_1,number_2):
        return number_1-number_2

class Multiplier (Calculator):
    def calculate(self,number_1,number_2):

        return number_1*number_2

class Divider  (Calculator):
    def calculate(self,number_1,number_2):
        if number_2==0:
            raise ZeroDivisionError("Ділення на нуль не можливе")
        return number_1/number_2

class Powerer (Calculator):
    def calculate(self,number_1,number_2):
        if number_1==0 and number_2 < 0:
            raise ValueError("зведення нуля в негативний степінь не можливо")
        return number_1**number_2




def main():
    print(" програма Калькулятор, для виходу наберіть exit")

    class ExitError(Exception):
        pass
    class NoNameOperEror(Exception):
        pass

    operations = {
        '+': Adder(),
        '-': Subtractor(),
        '*': Multiplier(),
        '/': Divider(),
        '^': Powerer()
    }
    while True:
        try:
            number_1= input("Введіть перше число  ")
            if number_1.lower() == "exit":
                raise ExitError(" Програму завершено, до-побачення")

            number_1 = float(number_1)

            number_2 =input("Введіть друге число  ")
            if number_2.lower() == "exit":
                raise ExitError(" Програму завершено, до-побачення")

            number_2 = float(number_2)

            oper= input(" Вкажіть дію для виконання (+, -, *, /, ^): ")
            if oper.lower== "exit":
                raise ExitError(" Програму завершено, до-побачення")

            if oper not in operations:
                raise NoNameOperEror (" не відома операція")


            result=round(operations[oper].calculate(number_1,number_2),2) #
            print(result)


        except ZeroDivisionError as zde:
            print(f" помилка: {zde} ")
            break
        except  ValueError as ve:
            print(f" помилка: {ve} ")
            break
        except  AttributeError as oe:
            print(f" помилка: {oe} ")
            break
        except ExitError as ee:
            print(ee)
            break
        except NoNameOperEror as nno:
            print(nno)


if __name__=="__main__":
    main()











