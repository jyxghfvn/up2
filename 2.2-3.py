class Numbers:
    def __init__(self, number1=0, number2=0):
        self.number1 = number1
        self.number2 = number2

    def info(self):
        print(f"Первое число = {self.number1}")
        print(f"Второе число = {self.number2}")

    def change_numbers(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def sum_numbers(self):
        print("Сумма этих чисел =", self.number1 + self.number2)

    def biggerthatnumber(self):
        if self.number1 == self.number2:
            print("Они равны")
        elif self.number2 > self.number1:
            print("Второе число больше первого")
        else:
            print("Первое число больше второго")


numbers = Numbers()

while True:
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
    except ValueError:
        print("Пожалуйста, вводите только числа.")
        continue

    numbers.change_numbers(num1, num2)

    numbers.info()
    numbers.sum_numbers()
    numbers.biggerthatnumber()

    cont = input("Хотите ввести новые числа? (да/нет): ").strip().lower()
    if cont != 'да':
        break

print("Программа завершена.")