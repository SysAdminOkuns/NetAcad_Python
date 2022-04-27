numbers = [10, 5, 7, 2, 1]
largest_num = -9999
print(numbers)
nList = []

for i in range((len(numbers))):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp
print(numbers)