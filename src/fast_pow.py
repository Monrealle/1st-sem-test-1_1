def fastPow(number, power):
    if power < 0:
        print("Степень не может быть отритцательной")
    if power == 0:
        return 1

    result = 1
    base = number
    while power > 0:
        if power % 2 == 1
            result *= base
        base *= base
        power = power // 2
    return result
