#   Напишите калькулятор, который будет осуществлять 6 операций: сложение, вычитание, умножение, деление, возведение в степень и выход из программы.
#   Операции с числами выполните в функциях.
#   Обработайте ошибку деления на 0 и реализуйте проверку на входные данные.


class Calc:
    def add(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Error. Enter nums.")
        return x + y

    def minus(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Error. Enter nums.")
        return x - y

    def multiply(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Error. Enter nums.")
        return x * y

    def divide(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Error. Enter nums.")
        if y == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")
        return x / y

    def exponent(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Error. Enter nums.")
        return x ** y


def main():
    calculator = Calc()
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Выход")

        choice = input("Введите номер операции: ")

        if choice == '6':
            break

        if choice not in ['1', '2', '3', '4', '5']:
            print("Error. Choose 1 - 5 .")
            continue

        num1_input = input("First num: ")
        num2_input = input("Second num: ")

        if not num1_input.replace('.', '', 1).replace('-', '', 1).isdigit():
            print("Error: ")
            continue

        if not num2_input.replace('.', '', 1).replace('-', '', 1).isdigit():
            print("Error: ")
            continue

        num1 = float(num1_input)
        num2 = float(num2_input)

        try:
            if choice == '1':
                result = calculator.add(num1, num2)
            elif choice == '2':
                result = calculator.minus(num1, num2)
            elif choice == '3':
                result = calculator.multiply(num1, num2)
            elif choice == '4':
                result = calculator.divide(num1, num2)
            elif choice == '5':
                result = calculator.exponent(num1, num2)
            print(result)
        except (TypeError, ZeroDivisionError, ValueError) as e:
            print("Error:", e)


if __name__ == "__main__":
    main()


