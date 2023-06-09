import math


def main(n):
    if n == 0:
        return 0.54
    elif n == 1:
        return -0.17
    else:
        a = math.pow(main(n - 1), 2)
        b = math.sqrt(math.pow(main(n - 1), 3) + math.pow(main(n - 2), 2))
        return a - b / 21


if __name__ == '__main__':
    print(main(9))
