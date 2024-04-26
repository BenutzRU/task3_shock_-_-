class Wallet:
    _valid_currencies = ["RUB", "USD", "EUR"]
    _payment_system = "xz"

    def __init__(self, name, currency):
        if currency not in Wallet._valid_currencies:
            print(f"Error: {currency}. Допустимые валюты: {Wallet._valid_currencies}")
            return

        self._name = name
        self._currency = currency
        self._balance = 0

    def top_up_balance(self):
        amount = input(f"Сумма пополнения ({self._currency}): ")
        if not amount.isdigit() or float(amount) <= 0:
            print("Сумма пополнения должна быть больше 0.")
            return

        self._balance += float(amount)

    def pay(self):
        amount = input(f"Enter sum ({self._currency}): ")
        if not amount.isdigit() or float(amount) <= 0:
            print("Сумма оплаты должна быть больше 0.")
            return

        if float(amount) > self._balance:
            print("Error.")
            return

        self._balance -= float(amount)

    def rename_wallet(self, new_name):
        if not new_name.strip():
            print("Error.")
            return

        self._name = new_name
        print(f"Кошелек переименован в '{self._name}'.")

    def get_balance_info(self):
        print(f"Баланс кошелька '{self._name}': {self._balance:.2f} {self._currency}")

    def delete_wallet(self):
        confirmation = input("Безвозвратно удалить кошелек? (да/нет): ")
        if confirmation.lower() == "да":
            self._balance = 0
            print("Кошелек удален.")
            return True
        else:
            print("Удаление кошелька отменено.")
            return False

wallet = Wallet("xzxz", "USD")

while True:
    print(f"\nМеню управления кошельком '{wallet._name}':")
    print("1. Пополнить баланс")
    print("2. Оплатить")
    print("3. Баланс кошелька")
    print("4. Удалить кошелек")
    print("5. Переименовать кошелек")
    print("0. Выход")

    choice = input("Выберите действие: ")
    if not choice.isdigit():
        print("Error. 0 - 5.")
        continue

    choice = int(choice)

    if choice == 1:
        wallet.top_up_balance()
    elif choice == 2:
        wallet.pay()
    elif choice == 3:
        wallet.get_balance_info()
    elif choice == 4:
        if wallet.delete_wallet():
            break
    elif choice == 5:
        new_name = input("Новое имя: ")
        wallet.rename_wallet(new_name)
    elif choice == 0:
        print("Завершение работы с кошельком.")
        break
    else:
        print("Error.")
