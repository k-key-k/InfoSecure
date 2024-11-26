import random


def num_generator_k_bit(bit):
    return random.randint(2 << (bit - 2), (2 << bit - 1) - 1)


def odd_num_generator_k_bit(bit):
    return (random.randint(2 << (bit - 2), (2 << bit - 1) - 1)) | 1
