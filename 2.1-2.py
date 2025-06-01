def comb(candidates, target):
    def backtrack(start, combinations, target):
        if target == 0:
            result.append(combinations)
            return
        if target < 0:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            backtrack(i + 1, combinations + [candidates[i]], target - candidates[i])

    candidates.sort()
    result = []
    backtrack(0, [], target)
    return result

candidates = list(map(int, input("candidates: ").split()))
target = int(input("target: "))
result = comb(candidates, target)
print("output: ", result)