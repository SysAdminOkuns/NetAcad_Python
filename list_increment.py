lst = [1, 2, 3, 4, 5]
lst_2 = []

add = 0

print(lst)

for num in lst:
    add += num
    lst_2.append(add)

print(lst_2)