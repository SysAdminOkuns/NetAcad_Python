numbers = [10, 5, 7, 2, 1]

list_len = len(numbers)

print("Before sort:",numbers)
i = 0
while i < list_len:
    j = i + 1
    while j < list_len:
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
        j += 1
    print(numbers)
    i += 1
print("After sort",numbers)
    