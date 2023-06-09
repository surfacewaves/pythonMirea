import math


def main(z=[], x=[], y=[]):
    result = 0
    for i in range(0, 7):
        a = math.pow(y[i], 2)
        b = math.pow(z[i], 3)
        c = x[6 - i]
        result += 40 * a - b / 66 - 49 * c
    return result


if __name__ == '__main__':
    print(main([-0.44, -0.18, -0.19, -0.12, 0.71, 0.41, 0.35],
               [-0.13, 0.35, -0.04, 0.1, 0.5, 0.25, -0.5],
               [0.43, 0.03, -0.31, 0.73, -0.3, -0.47, -0.08]))
