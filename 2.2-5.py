class MyClass:
    def __init__(self, meaning1="Свойство по умолчанию", meaning2="Нет данных"):
        self.meaning1 = meaning1
        self.meaning2 = meaning2

    def info(self):
      print(f"Значение: {self.meaning1}")
      print(f"Значение1: {self.meaning2}")

    def __del__(self):
        print("Удалено")

myclass = MyClass("Хелоу", "Ворлд")
myclass.info()

myclass_default = MyClass()
myclass_default.info()

myclass.meaning1 = "Hello"
myclass.meaning2 = "World"
myclass.info()

myclass.__del__()