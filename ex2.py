import math


def f1(z):
    return 82 * math.pow(z / 86 - 87 * math.pow(z, 3), 6)


def f2(z):
    a = math.pow(math.cos(1 - math.pow(z, 3)), 5)
    b = 98 * math.pow(z, 4) + 31 * math.pow(math.cos(22 * z), 7)
    return a + b


def f3(z):
    return math.pow(z, 7) + 1


def f4(z):
    return 10 * math.fabs(z)


def f5(z):
    a = math.exp(z) / 59
    b = math.pow(math.tan(2 + 58 * z + 30 * math.pow(z, 2)), 5)
    return a - b


def main(z):
    if z < 43:
        result = f1(z)
        return result
    elif 43 <= z < 111:
        result = f2(z)
        return result
    elif 111 <= z < 151:
        result = f3(z)
        return result
    elif 151 <= z < 190:
        result = f4(z)
        return result
    else:
        result = f5(z)
        return result


if __name__ == '__main__':
    print(main(48))
