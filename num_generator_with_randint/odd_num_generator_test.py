from num_generator_k_bit import odd_num_generator_k_bit
from num_generator_getrandbits import odd_num_generator_getrandbits

for i in range(10, 101, 10):
    for j in range(1000):
        num = odd_num_generator_k_bit(i)
        if num.bit_length() != i and num % 2 == 0:
            print(num)
    print(f"числа с битностью {i} прошли проверку")

for i in range(10, 101, 10):
    for j in range(1000):
        num = odd_num_generator_getrandbits(i)
        if num.bit_length() != i and num % 2 == 0:
            print(num)
    print(f"числа с битностью {i} прошли проверку")