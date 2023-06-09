import math


def main(z, x, y):
    f1 = math.sqrt(math.pow(math.sqrt(y + math.pow(z, 2) + math.pow(x, 3)), 5))
    f2 = math.pow(math.fabs((math.pow(z, 2) / 34) - math.pow(y, 3) - y), 4)
    f3 = math.pow(math.asin(x), 7)
    return f1 + 51 * f2 + 40 * f3


if __name__ == '__main__':
    print(main(0.55, 0.82, 0.63))
