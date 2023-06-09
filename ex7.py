def work7(input_number):
    input_number = int(input_number, 16)
    n1 = input_number & ((1 << 18) + (1 << 8))
    n2 = input_number & ((1 << 18) + ((2 ** 4 - 1) << 4))
    n3 = input_number & ((1 << 18) + (3 << 2))
    n4 = input_number & ((1 << 18) + 3)

    return n4, n3 >> 2, n2 >> 4, n1 >> 8
