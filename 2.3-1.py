class Worker:
    def __init__(self,name = "name",surname = "surname",rate = 0,days = 0):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def GetSalary(self):
        return print("Зарплата: ",self.rate * self.days)

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Ставка: {self.rate}")
        print(f"Количество отработаных дней: {self.days}")

men = Worker("Иван","Иванов",777,7)
men.info()
men.GetSalary()