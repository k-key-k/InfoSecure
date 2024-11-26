import random


def num_generator_getrandbits(k):
    num = random.getrandbits(k)

    if num < (1 << (k - 1)):
        num += (1 << (k - 1))

    return num


def odd_num_generator_getrandbits(k):
    num = random.getrandbits(k) | 1

    if num < (1 << (k - 1)):
        num += (1 << (k - 1))

    return num