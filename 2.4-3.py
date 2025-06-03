import datetime
import sqlite3
import psutil

class DataBas:
    def __init__(self, db_name="MonitoringPC.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect_db()
        self.create_table()

    def connect_db(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS monitor (
            time TEXT,
            CPU_percent REAL,
            memory_percent REAL,
            disk_percent REAL
        )""")
        self.connection.commit()

    def insert_data(self, cpu_percent, memory_percent, disk_percent):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO monitor (time, CPU_percent, memory_percent, disk_percent) VALUES (?, ?, ?, ?)",
                            (timestamp, cpu_percent, memory_percent, disk_percent))
        self.connection.commit()

    def view_all_monitoringPC(self):
        self.cursor.execute("SELECT * FROM monitor")
        monitor = self.cursor.fetchall()
        if monitor:
            for i in monitor:
                print(i)
        else:
            print("")

    def close(self):
        if self.connection:
            self.connection.close()


monitoring = DataBas()
print("Меню:", "\n",
        1, "- старт", "\n",
        0, "- выход", "\n")

exit_code = int(input("Вы выбрали: "))

while exit_code != 0:
    print("\nМеню:")
    print("1 - Просмотр текущего состояния ПК")
    print("2 - Просмотр сохранённых данных о вашем ПК")
    print("0 - выход")
    choice = input("Вы выбрали: ")

    if choice == "1":
        CPU = psutil.cpu_percent()
        print(f"Использование CPU: {CPU}%")
        RAM = psutil.virtual_memory().percent
        print(f"Использование памяти: {RAM}%")
        SSD = psutil.disk_usage('/').percent
        print(f"Использование диска: {SSD}%")
        monitoring.insert_data(CPU, RAM, SSD)
    elif choice == "2":
        monitoring.view_all_monitoringPC()
    elif choice == "0":
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите номер из меню.")

    print("\nМеню:", "\n",
            1, "- вы хотите продолжить? ", "\n",
            0, "- выход", "\n")
    exit_code = int(input("Вы выбрали: "))

monitoring.close()
print("Конец программы")