from num_generator_with_randint.num_generator_getrandbits import num_generator_getrandbits
from num_generator_with_randint.num_generator_k_bit import num_generator_k_bit


for i in range(10, 101, 10):
    for j in range(10000):
        num = num_generator_k_bit(i)
        if num.bit_length() != i:
            print(num)
    print(f"числа с битностью {i} прошли проверку")

for i in range(10, 101, 10):
    for j in range(10000):
        num = num_generator_getrandbits(i)
        if num.bit_length() != i:
            print(num)
    print(f"числа с битностью {i} прошли проверку")