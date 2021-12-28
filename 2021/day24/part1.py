def main():
    # stack = [d1+12, d2+9, d3+8]

    # # stack.pop()
    # d4 =d3 + 8 -8
    # stack = [d1+12, d2+9,d5+0, d6+11, d7+10]
    # # stack.pop()
    # d8 = d7+10 - 11
    # stack = [d1+12, d2+9,d5+0, d6+11, d9+3]
    # #stack.pop()
    # d10 = d9+3 - 1
    # stack = [d1+12, d2+9,d5+0, d6+11]
    # #stack.pop()
    # d11 = d6+11 - 8
    # stack = [d1+12, d2+9,d5+0]
    # #stack.pop()
    # d12 = d5+0 - 5
    # stack = [d1+12, d2+9]
    # #stack.pop()
    # d13 = d2+9 - 16
    # stack = [d1+12]
    # #stack.pop()
    # d14 = d1+12 - 6

    # d4 =d3
    # # 9 = 9 // d4 = 9, d3 = 9
    # # 1 = 1 // d4 = 1, d3 = 1
    # d8 = d7 - 1
    # # 8 = 9 - 1 // d8 = 8, d7 = 9
    # # 1 = 2 - 1 // d8 = 1, d7 = 2
    # d10 = d9 + 2
    # # 9 = 7 + 2 // d10 = 9, d9 = 7
    # # 3 = 1 + 2 // d10 = 3, d9 = 1
    # d11 = d6 + 3
    # # 9 = 6 + 3 // d11 = 9, d6 = 6
    # # 4 = 1 + 3 // d11 = 4, d6 = 1
    # d12 = d5 - 5
    # # 4 = 9 - 5 // d12 = 4, d5 = 9
    # # 1 = 6 -5 // d12 = 1, d5 = 6
    # d13 = d2 - 7
    # # 2 = 9 - 7 // d13 = 2, d2 = 9
    # # 1 = 8 - 7 // d13 = 1, d2 = 8
    # d14 = d1+6
    # # 9 = 3 + 6 // d14 = 9, d1 = 3
    # # 7 = 1 + 6 // d14 = 7, d1 = 1

    # # p1
    # 39999698799429

    # #p2
    # 18116121134117

    # digits = [3, 9, 9, 9, 9, 6, 9, 8, 7, 9, 9, 4, 2, 9]
    digits = [1, 8, 1, 1, 6, 1, 2, 1, 1, 3, 4, 1, 1, 7]

    x = 0
    z = 0
    y = 0

    w = digits[0]
    x = 1
    y = w
    y += 12
    z += y

    w = digits[1]
    x = 1
    z = z * 26
    y = w
    y += 9
    z += y

    w = digits[2]
    x = 1
    z = z * 26
    y = w
    y += 8
    z += y

    w = digits[3]
    x = z
    x = x % 26
    z = z // 26
    x += -8

    x = 1 if x == w else 0
    x = 1 if x == 0 else 0

    y = 25
    y = y * x
    y += 1
    z = z * y
    y = w
    y += 3
    y = y * x
    z += y

    w = digits[4]
    x = 1
    z = z * 26
    y = w
    z += y

    w = digits[5]
    x = 1
    z = z * 26
    y = w
    y += 11
    z += y

    w = digits[6]
    x = 1
    z = z * 26
    y = w
    y += 10
    z += y

    w = digits[7]
    x = z
    x = x % 26
    z = z // 26
    x += -11

    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 25
    y = y * x
    y += 1

    z = z * y

    y = w
    y += 13
    y = y * x
    z += y

    w = digits[8]
    x = 1
    z = z * 26
    y = w
    y += 3
    z += y

    w = digits[9]
    x = z
    x = x % 26
    z = z // 26
    x += -1

    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 25
    y = y * x
    y += 1
    z = z * y
    y = w
    y += 10
    y = y * x
    z += y

    w = digits[10]
    x = z
    x = x % 26
    z = z // 26
    x += -8

    x = 1 if x == w else 0
    x = 1 if x == 0 else 0

    y = 25
    y = y * x
    y += 1
    z = z * y
    y = w
    y += 10
    y = y * x
    z += y

    w = digits[11]
    x = z
    x = x % 26
    z = z // 26
    x += -5

    x = 1 if x == w else 0
    x = 1 if x == 0 else 0

    y = 25
    y = y * x
    y += 1
    z = z * y
    y = w
    y += 14
    y = y * x
    z += y

    w = digits[12]
    x = z
    x = x % 26
    z = z // 26
    x += -16

    x = 1 if x == w else 0
    x = 1 if x == 0 else 0

    y = 25
    y = y * x
    y += 1
    z = z * y
    y = w
    y += 6
    y = y * x
    z += y

    w = digits[13]
    x = z
    x = x % 26
    z = z // 26
    x += -6

    x = 1 if x == w else 0
    x = 1 if x == 0 else 0

    y = 25
    y = y * x
    y += 1
    z = z * y
    y = w
    y += 5
    y = y * x
    z += y

    print(z)
    if z == 0:
        print("got a valid number")


main()