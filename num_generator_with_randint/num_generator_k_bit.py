import random


def num_generator_k_bit(bit):
    if bit <= 0:
        return EOFError("bit most be > 0")
    elif bit <= 1:
        return random.randint(0, 1)
    else:
        return random.randint(2 << (bit - 2), (2 << bit - 1) - 1)


def odd_num_generator_k_bit(bit):
    if bit <= 0:
        return EOFError("bit most be > 0")
    elif bit <= 1:
        return random.randint(0, 1)
    else:
        return (random.randint(2 << (bit - 2), (2 << bit - 1) - 1)) | 1
