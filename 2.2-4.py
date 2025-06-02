from random import randint

class Counter:
    def __init__(self,number):
        self.number = number
    def increase_number(self):
        self.number += 1
    def reduce_number(self):
        self.number -= 1
    def info(self):
        print(f"Ваше число: {self.number}")
    def randomNumber(self):
        self.number = randint(1,100)
    def default(self,number):
        self.number = number
x = int(input("Введите число: "))
number = Counter(x)
exit_program = int(input("1 - начать работу, 0 - выйти\n"))
while exit_program == 1:
    print("Информация:","\n",
          "1 - Увеличить число на единицу","\n",
          "2 - Уменьшить число на единицу","\n",
          "3 - Информация","\n",
          "4 - Назначить случайное значение", "\n",
          "5 - Назначить число по умолчанию", "\n",
          "0 - Выход")
    a = int(input())
    if a == 1:
        number.increase_number()
        number.info()
    elif a == 2:
        number.reduce_number()
        number.info()
    elif a == 3:
        number.info()
    elif a == 4:
        number.randomNumber()
        number.info()
    elif a == 5:
        number.default(x)
        number.info()
    elif a == 0:
        exit_program = int(input("1 - продолжить|| 0 - выйти\n"))