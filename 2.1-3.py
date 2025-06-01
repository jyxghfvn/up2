def comparator(nums):
    newnums = set(nums)
    if len(newnums) == len(nums):
        return False
    else:
        return True
nums = list(map(int, input("Ввод:\n").split()))
result = comparator(nums)
print("Вывод:\n", result)