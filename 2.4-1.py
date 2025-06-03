import sqlite3

class Student:
    def __init__(self, name, surname, patronymic, group, evaluations):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group = group
        self.evaluations = evaluations

    def info_name(self):
        return self.name
    def info_surname(self):
        return self.surname
    def info_patronymic(self):
        return self.patronymic
    def info_group(self):
        return self.group
    def info_evaluations(self):
        return self.evaluations

class DataBas:
    def __init__(self, db_name="Students.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect_db()
        self.create_table()

    def connect_db(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS student (
            name TEXT,
            surname TEXT,
            patronymic TEXT,
            "group" TEXT,
            evaluations TEXT
        )""")
        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()

    def add_student(self, student):
        self.cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?)", (
            student.info_name(), student.info_surname(), student.info_patronymic(),
            student.info_group(), str(student.info_evaluations())))
        self.connection.commit()
        print("Студент был добавлен.")

    def view_all_students(self):
        self.cursor.execute("SELECT * FROM student")
        students = self.cursor.fetchall()
        if students:
            for student in students:
                print(student)
        else:
            print("")

    def viev_student_and_ball(self,surname):
        self.cursor.execute("SELECT * FROM student WHERE surname = ?", (surname,))
        student_data = self.cursor.fetchone()
        if student_data:
            name, surname, patronymic, group, evaluations_str = student_data
            evaluations = [int(i) for i in evaluations_str.strip("[]").split(", ")]
            average_grade = sum(evaluations) / len(evaluations)
            print("Информация о студенте:", name, surname, patronymic, "Группы: ", group)
            print("Его оценки: ", evaluations)
            print("Средний балл: ", average_grade)
        else:
            print("Студент с такой фамилией не найден.")

    def edit_student(self,surname):
        self.cursor.execute("SELECT * FROM student WHERE surname = ?", (surname,))
        student_data = self.cursor.fetchone()
        if student_data:
            name, surname, patronymic, group, evaluations = student_data
            new_name = input("Введите новое Имя Студента: ")
            new_surname = input("Введите новую Фамилию Студента: ")
            new_patronymic = input("Введите новое Отчество Студента: ")
            new_group = input("Введите новую Группу Студента: ")
            new_evaluations = []
            for i in range(4):
                grade = int(input(f"Введите новую оценку {i + 1}: "))
                new_evaluations.append(grade)
            Student1 = Student(new_name, new_surname, new_patronymic, new_group, str(new_evaluations))
            self.cursor.execute("UPDATE student SET name = ? WHERE name = ?", (Student1.info_name(), name))
            self.cursor.execute("UPDATE student SET surname = ? WHERE surname = ?",
                                  (Student1.info_surname(), surname))
            self.cursor.execute("UPDATE student SET patronymic = ? WHERE patronymic = ?",
                                  (Student1.info_patronymic(), patronymic))
            self.cursor.execute("UPDATE student SET 'group' = ? WHERE 'group' = ?", (Student1.info_group(), group))
            self.cursor.execute("UPDATE student SET evaluations = ? WHERE evaluations = ?",
                                  (Student1.info_evaluations(), evaluations))
            self.connection.commit()
        else:
            print("Студент с такой фамилией не найден.")

    def del_student(self,surname):
        self.cursor.execute("SELECT * FROM student WHERE surname = ?", (surname,))
        student_data = self.cursor.fetchone()
        if student_data:
            self.cursor.execute("DELETE FROM student WHERE surname=?", (surname,))
        else:
            print("Студент с такой фамилией не найден.")
        self.connection.commit()

    def view_group_average(self,group):
        self.cursor.execute("SELECT evaluations FROM student WHERE \"group\" = ?", (group,))
        evaluations_mas = self.cursor.fetchall()
        if evaluations_mas:
            counter = 0
            counter_student = 0
            for evaluations_tuple in evaluations_mas:
                evaluations_str = evaluations_tuple[0]
                evaluations = [int(i) for i in evaluations_str.strip("[]").split(", ")]
                grade = sum(evaluations) / len(evaluations)
                counter += grade
                counter_student += 1
            a = counter / counter_student
            print(f"Средний балл: ", a)
        else:
            print("Группа не найдена")

db_manager = DataBas()

print("Меню:\n",
        1, "- начать работу", "\n",
        0, "- выход", "\n")

exit_code = int(input("Вы выбрали: "))

while exit_code != 0:
    print("\nМеню:")
    print("1 - Добавить нового студента")
    print("2 - Просмотр всех студентов")
    print("3 - Просмотр выбранного студента вместе с его средним баллом")
    print("4 - Редактировать студента")
    print("5 - Удалить студента")
    print("6 - Посмотреть средний балл группы")
    print("0 - выход")

    choice = int(input("Вы выбрали: "))
    if choice == 1:
        name = input("Введите Имя Студента: ")
        surname = input("Введите Фамилию Студента: ")
        patronymic = input("Введите Отчество Студента: ")
        group = input("Введите Группу Студента: ")
        evaluations = []
        for i in range(4):
            grade = int(input(f"Введите оценку {i + 1}: "))
            evaluations.append(grade)
        Student1 = Student(name, surname, patronymic, group, evaluations)
        db_manager.add_student(Student1)
    elif choice == 2:
        db_manager.view_all_students()
    elif choice == 3:
        surname = input("Введите фамилию студента для поиска: ")
        db_manager.viev_student_and_ball(surname)
    elif choice == 4:
        surname = input("Введите фамилию студента для редакции: ")
        db_manager.edit_student(surname)
    elif choice == 5:
        surname = input("Введите фамилию студента для УДАЛЕНИЯ)- ")
        db_manager.del_student(surname)
    elif choice == 6:
        group = input("Введите группу студентов для вывода среднего бала: ")
        db_manager.view_group_average(group)
    elif choice == 0:
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите нужную цифру из меню.")

    print("\nМеню:\n",
            1, "- продолжить", "\n",
            0, "- выход", "\n")
    exit_code = int(input("Вы выбрали: "))

db_manager.close()
print("Конец.")
