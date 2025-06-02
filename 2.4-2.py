import sqlite3

class DataBas:
    def __init__(self, db_name="ILoveDrink.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect_db()
        self.create_table()

    def connect_db(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            quantity REAL,
            unit TEXT
        )""")
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS drinks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            alcohol_strength,
            quantity REAL,
            unit TEXT
        )""")
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS cocktails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            structure TEXT,
            alcohol_strength REAL,
            price REAL
        )""")
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS sell (
            name TEXT UNIQUE,
            choice_drinks TEXT,
            quantity INTEGER
        )""")
        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()

    def add_ingredients(self, name, quantity, unit):
        self.cursor.execute("""
        INSERT OR REPLACE INTO ingredients (name, quantity, unit) VALUES (?, ?, ?)""", (name, quantity, unit))
        self.connection.commit()

    def add_drink(self, name,alcohol_strength, quantity, unit):
        self.cursor.execute("""
        INSERT OR REPLACE INTO drinks (name,alcohol_strength, quantity, unit) VALUES (?, ?, ?, ?)""", (name, alcohol_strength, quantity, unit))
        self.connection.commit()

    def add_cocktail(self,name, structure,alcohol_strength, price):
        self.cursor.execute("""
                INSERT OR REPLACE INTO cocktails (name,structure, alcohol_strength, price) VALUES (?, ?, ?, ?)""",
                            (name, structure, alcohol_strength, price))
        self.connection.commit()

    def all_drinks(self):
        print("_________________________Напитки_________________________")
        self.cursor.execute("SELECT * FROM drinks")
        drinks = self.cursor.fetchall()
        if drinks:
            for j in drinks:
                print(j)
        else:
            print("")

    def all_ingredients(self):
        print("________________________Ингредиенты_______________________")
        self.cursor.execute("SELECT * FROM ingredients")
        ingredients = self.cursor.fetchall()
        if ingredients:
            for j in ingredients:
                print(j)
        else:
            print("")

    def all_cocktails(self):
        print("________________________Коктейли_______________________")
        self.cursor.execute("SELECT * FROM cocktails")
        cocktail = self.cursor.fetchall()
        if cocktail:
            for j in cocktail:
                print(j)
        else:
            print("")


    def add_drinks_remove(self, choice_drinks,name,quantity, no):
        self.cursor.execute(f"SELECT quantity FROM {choice_drinks} WHERE name=?", (name,))
        row = self.cursor.fetchone()
        if no == 4:
            if row:
                current_quantity = row[0]
                if current_quantity >= quantity:
                    new_quantity = current_quantity - quantity
                    self.cursor.execute(f"UPDATE {choice_drinks} SET quantity=? WHERE name=?", (new_quantity, name))
                    self.connection.commit()
        elif no == 6:
            if row:
                current_quantity = row[0]
                if current_quantity >= quantity:
                    new_quantity = current_quantity + quantity
                    self.cursor.execute(f"UPDATE {choice_drinks} SET quantity=? WHERE name=?", (new_quantity, name))
                    self.connection.commit()
        else:
            print("Продукт не найден")

    def sell(self,name,quantity, choice_drinks):
        self.cursor.execute("""
                INSERT OR REPLACE INTO sell (name,choice_drinks, quantity) VALUES (?, ?, ?)""", (name,choice_drinks, quantity))
        self.connection.commit()
    def info_sell(self):
        print("_______________________Продажи_______________________")
        self.cursor.execute("SELECT * FROM sell")
        sell = self.cursor.fetchall()
        if sell:
            for j in sell:
                print(j)
        else:
            print("")





ILD_manadger = DataBas()
alcohol_strength = {"Водка": 36, "Квас": 2, "Светлое Пиво": 4, "Крепкое Пиво": 8, "Джин-тоник": 7,
                    "Шампанское": 9, "Вино": 9, "Портвейн": 17, "Настойка сладкая": 18, "Настойка горькая": 30,
                    "Ликер": 15, "Бренди": 38, "Водка русская": 40, "Коньяк": 45, "Джин": 35, "Текила": 35, "Чача": 45,
                    "Виски": 40, "Ром": 65, "Самогон": 80, "Абсент": 75}

print("Меню:" "\n", 1, "- начать работу", "\n", 0, "- выход", "\n")

exit_code = int(input("Вы выбрали: "))

while exit_code != 0:
    print("\nМеню:")
    print("1 - Добавить ингредиент")
    print("2 - Добавить напиток")
    print("3 - Создать коктейль")
    print("4 - Убавить товар")
    print("5 - Посмотреть остатки")
    print("6 - Пополнить запасы")
    print("7 - Продать товар")
    print("8 - Просмотр количества проданного товара")
    print("0 - Выйти")

    choice = int(input("Вы выбрали: "))
    if choice == 1:
        name = input("Введите название ингредиента: ")
        quantity = input("Введите количество ингредиента в миллилитрах: ")
        unit = "мил."
        ILD_manadger.add_ingredients(name,quantity, unit)
    elif choice == 2:
        name = input("Введите название напитка: ")
        quantity = input("Введите количество напитка в миллилитрах: ")
        unit = "мил."
        alcohol_strength_n = 10
        for key, value in alcohol_strength.items():
            if name == key:
                alcohol_strength_n = alcohol_strength[key]
                ILD_manadger.add_drink(name, alcohol_strength_n, quantity, unit)
                break
    elif choice == 3:
        # Крепость коктейля можно вычислить по формуле: ABV
        # коктейля = ∑(Объём каждого алкогольного ингредиента × Крепость ингредиента) / Общий объём коктейля × 100.
        quantity_volume = 0
        alcohol_strength_volume = 0
        name = input("Введите название коктейля: ")
        price = float(input("Введите цену коктейля: "))
        print("Введите состав коктейля. Для завершения введите 'стоп'.")
        structure = []
        while True:
            alcohol_strength_n = 0
            print("Вот список имеющихся ингредиентов и алкогольных напитков")
            ILD_manadger.all_drinks()
            ILD_manadger.all_ingredients()
            ing_name = input("Ингредиент что вы хотите добавить: ")
            for key, value in alcohol_strength.items():
                if ing_name == key:
                    alcohol_strength_n = alcohol_strength[key]
                    break
            if ing_name.lower() == 'стоп':
                break
            amount = float(input("Количество(миллилитры): "))
            quantity_volume += amount
            alcohol_strength_volume += amount * alcohol_strength_n
            structure.append((ing_name, amount))
        alcohol_strength_cocktail = alcohol_strength_volume/quantity_volume
        ILD_manadger.add_cocktail(name, str(structure),alcohol_strength_cocktail, price)
    elif choice == 4:
        print("Что вы хотите убавить:")
        print("1 - ингредиент")
        print("2 - напиток")
        choice_drinks = int(input("Ваш выбор - "))
        if choice_drinks == 1:
            choice_drinks = "ingredients"
            ILD_manadger.all_ingredients()
        elif choice_drinks == 2:
            choice_drinks = "drinks"
            ILD_manadger.all_drinks()
        else:
            print("Неправильно, попробуйте ещё раз")
        name = input("Название: ")
        quantity = float(input("Количество: "))
        ILD_manadger.add_drinks_remove(choice_drinks,name,quantity,choice)
    elif choice == 5:
        ILD_manadger.all_ingredients()
        ILD_manadger.all_drinks()
        ILD_manadger.all_cocktails()
        print("_________________________________________________________")
    elif choice == 6:
        print("Что вы хотите пополнить:")
        print("1 - ингредиент")
        print("2 - напиток")
        choice_drinks = int(input("Ваш выбор - "))
        if choice_drinks == 1:
            choice_drinks = "ingredients"
            ILD_manadger.all_ingredients()
        elif choice_drinks == 2:
            choice_drinks = "drinks"
            ILD_manadger.all_drinks()
        else:
            print("Неправильно, попробуйте ещё раз")
        name = input("Название: ")
        quantity = float(input("Количество: "))
        ILD_manadger.add_drinks_remove(choice_drinks, name, quantity,choice)
    elif choice == 7:
        print("Что вы хотите купить:")
        print("1 - ингредиент")
        print("2 - напиток")
        print("3 - коктейль")
        choice_drinks = int(input("Ваш выбор - "))
        if choice_drinks == 1:
            choice_drinks = "ingredients"
            ILD_manadger.all_ingredients()
        elif choice_drinks == 2:
            choice_drinks = "drinks"
            ILD_manadger.all_drinks()
        elif choice_drinks == 3:
            choice_drinks = "cocktails"
            ILD_manadger.all_cocktails()
        else:
            print("Неправильно, попробуйте ещё раз")
        name = input("Введите что вы хотите купить - ")
        quantity = int(input("Введите сколько вы хотите купить (шт.): "))
        ILD_manadger.sell(name,quantity,choice_drinks)
    elif choice == 8:
        ILD_manadger.info_sell()
    elif choice == 0:
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите номер из меню.")

ILD_manadger.close()
print("Конец")