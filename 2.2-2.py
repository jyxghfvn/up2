class Train:
    def __init__(self, name="Нет данных", number="Нет данных", time="Нет данных"):
        self.name = name
        self.number = number
        self.time = time

    def info_number(self):
        return self.number

    def changes_name(self, name):
        self.name = name

    def changes_time(self, time):
        self.time = time

    def info(self):
        print(f"Пункт назначения: {self.name}")
        print(f"Номер поезда: {self.number}")
        print(f"Время отправления: {self.time}")

Train1 = Train("Новосибирск", "896Н", "06:55")
Train2 = Train("Москва", "637Н", "12:51")
Train3 = Train("Бийск", "401Н", "17:25")
Train4 = Train("Адлер", "115Н", "16:02")

mas = [Train1, Train2, Train3]

print("\n______________\n")
Train1.info()
print("\n______________\n")
Train2.info()
print("\n______________\n")
Train3.info()
print("\n______________\n")
Train4.info()
print("\n______________\n")

exit_program = int(input("1 - редактировать, 0 - выход\n"))
while exit_program != 0:
    a = input("Введите номер поезда ")
    found = False
    for i in range(len(mas)):
        if mas[i].info_number() == a:
            print("Замена данных\n")
            newname = input("Редактировать пункт назначения: ")
            mas[i].changes_name(newname)
            newtime = input("Редактировать время поезда: ")
            mas[i].changes_time(newtime)
            print("\n______Новая_информация______\n")
            mas[i].info()
            print("\n______________________________\n")
            found = True
            break

    if not found:
        print("Поезд с таким номером не найден.")

    exit_program = int(input("1 - продолжить редактировать, 0 - выход\n"))