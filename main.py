t = 0
J = input("Ввод:\n")
S = input()

for i in S:
    if J.count(i) > 0:
        t += 1
    else:
        continue
print("Вывод:\n", t)