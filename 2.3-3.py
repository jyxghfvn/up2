class Calculation:

    def __init__(self):
        self.calculationLine = ""

    def SetCalculationLine(self, new_line):
        self.calculationLine = new_line

    def SetLastSymbolCalculationLine(self, symbol):
        self.calculationLine += symbol

    def GetCalculationLine(self):
        return self.calculationLine

    def GetLastSymbol(self):
        if self.calculationLine:
            return self.calculationLine[-1]
        else:
            return ""

    def DeleteLastSymbol(self):
        self.calculationLine = self.calculationLine[:-1]

myclass = Calculation()

myclass.SetCalculationLine("Hello world")
print("Изменилось: ", myclass.GetCalculationLine())
myclass.SetLastSymbolCalculationLine("!!")
print("Добавился символ: ", myclass.GetCalculationLine())
print("Последний символ: ", myclass.GetLastSymbol())
myclass.DeleteLastSymbol()
print("Удалился последний символ: ", myclass.GetCalculationLine())
myclass.DeleteLastSymbol()
print("Удалился последний символ х2: ", myclass.GetCalculationLine())
print("Последний символ: ", myclass.GetLastSymbol())
myclass.SetCalculationLine("")
print("", myclass.GetLastSymbol())