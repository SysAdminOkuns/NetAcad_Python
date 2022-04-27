c0 = int(input("Enter c0: "))

if c0 > 1:
    steps = 0
    while c0 != 1:
        if c0 % 2 != 0:
            cnew = 3 * c0 + 1
        else:
            cnew = c0 // 2
        print(c0)
        c0 = cnew
        steps += 1
    print("steps =", steps)
else:
    print("Bad c0 value")