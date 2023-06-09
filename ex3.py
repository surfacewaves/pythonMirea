import math


def main(b, n, a, z):
    sumK = 0
    for k in range(1, a + 1):
        prN = 1
        for i in range(1, n + 1):
            sumB = 0
            for j in range(1, b + 1):
                x = math.pow((j + 77 * math.pow(z, 2)), 4)
                y = math.pow(math.log(j + math.pow(k, 3) + math.pow(i, 2)), 2)
                sumB += x - 8 * y
            prN *= sumB
        sumK += prN
    result = sumK
    return result


if __name__ == '__main__':
    print(main(2, 8, 3, 0.88))
