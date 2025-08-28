def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            try:
                ratio = values[i] / values[j]
                results.append((i, j, ratio))
            except ZeroDivisionError:
                results.append((i, j, "Division by zero"))
    return results

nums = [5, 10, 0, 20, 25]
print(compute_ratios(nums))
