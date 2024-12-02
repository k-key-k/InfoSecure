import random


def num_generator_getrandbits(k):
    num = random.getrandbits(k)

    if k <= 0:
        return EOFError("bit most be > 0")
    elif k <= 1:
        return random.getrandbits(k)
    else:
        if num < (1 << (k - 1)):
            num += (1 << (k - 1))

        return num


def odd_num_generator_getrandbits(k):
    num = random.getrandbits(k) | 1

    if k <= 0:
        return EOFError("bit most be > 0")
    elif k <= 1:
        return random.getrandbits(k)
    else:
        if num < (1 << (k - 1)):
            num += (1 << (k - 1))

        return num