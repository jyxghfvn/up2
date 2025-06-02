class Worker:
    def __init__(self, name = "name", surname = "surname", rate = 0, days = 0):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def getter_name(self):
        return print(f"Имя: {self.__name}")

    def getter_surname(self):
        return print(f"Фамилия: {self.__surname}")

    def getter_rate(self):
        return print(f"Ставка: {self.__rate}")

    def getter_days(self):
        return print(f"Количество отработаных дней: {self.__days}")

    def getter_salary(self):
        return self.__rate * self.__days

    def info(self):
        print(f"Имя: {self.__name}")
        print(f"Фамилия: {self.__surname}")
        print(f"Ставка: {self.__rate}")
        print(f"Количество отработаных дней: {self.__days}")


men = Worker("Иван", "Иванов", 777, 7)
men.info()
print("Зарплата: ", men.getter_salary())

print("Приватная информация")
men.getter_name()
men.getter_surname()
men.getter_rate()
men.getter_days()