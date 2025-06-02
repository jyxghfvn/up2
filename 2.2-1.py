class Student:

    def __init__(self, surname = "Нет данных", bdate = "Нет данных", groupnum = "Нет данных",grades = "Нет данных"):
        self.surname = surname
        self.bdate = bdate
        self.groupnum = groupnum
        self.grades = grades

    def change_surname(self, surname):
        self.surname = surname

    def change_bdate(self, bdate):
        self.data = bdate

    def change_groupnum(self, groupnum):
       self.groupnum = groupnum

    def changes_grades(self, grades):
        self.grades = grades

    def displayinfo(self):
        print(f"Фамилия: {self.surname}")
        print(f"Дата рождения: {self.bdate}")
        print(f"Номер группы: {self.groupnum}")
        print(f"Успеваемость: {self.grades}")

print("0 - выход\nДля продолжения нажмите любую кнопку")
a = input()
while a != "0":
    print("1 - редактировать пользователя 0 - выход")
    a = input()
    Student1 = Student()
    if a == "1":
        surname = input("Введите Фамилию ")
        Student1.change_surname(surname)
        bdate = input("Введите дату рождения ")
        Student1.change_bdate(bdate)
        groupnum = int(input("Введите номер группы "))
        Student1.change_groupnum(groupnum)
        grades = []
        for i in range(5):
            grade = int(input(f"Введите оценку {i + 1}: "))
            grades.append(grade)
        Student1.changes_grades(grades)
        Student1.displayinfo()
    else:
        Student1.displayinfo()
    print("Для продолжения нажмите любую кнопку\n0 - выход")
    a = input()