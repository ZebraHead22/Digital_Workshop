class BankAccount:

    @classmethod
    def create_empty_account(cls, data):
        __account_number = data
        __balance = 0
        return cls(float(__balance), __account_number)

    @staticmethod
    def __validate_balance(value):
        return value >= 0 and isinstance(value, (int, float))
            
    @staticmethod
    def validate_account_number(account_number):
        return isinstance(account_number, str)
    
    def __init__(self, balance, account_number):
        # self.__balance = balance
        # self.__account_number = account_number # Простой подход без всяких проверок
        
        if not self.__validate_balance(balance):
            raise ValueError (f"Amount must be a positive!")
        else: 
            self.__balance = balance

        if not self.validate_account_number(account_number):
            raise TypeError (f"account_number must be a string format!")
        else: 
            self.__account_number = account_number

        

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, balance):
        if balance > 0 and isinstance(balance, (float, int)):
            self.__balance = balance
        print(self.balance)
    
    
    def deposit(self, amount):
        """Пополнение счёта"""
        if amount > 0:
            self.__balance += amount
            print(f"Баланс пополнен на {amount}. Текущий баланс: {self.__balance}")
        else:
            print("Сумма должна быть положительной!")

    def withdraw(self, amount):
        """Снятие денег с проверки пин-кода"""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Снято {amount}. Остаток: {self.__balance}")
        else:
            print("Недостаточно средств или неверная сумма!")

    def get_balance(self):
        """Метод для просмотра баланса"""
        return self.__balance
        
try:
    acc = BankAccount.create_empty_account(123456789)  
except ValueError as e1:
    print(e1)
except TypeError as e2:
    print(e2)
finally:
    print("Some phrase")

