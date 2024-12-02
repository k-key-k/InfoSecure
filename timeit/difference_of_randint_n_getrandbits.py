import timeit
from num_generator_with_randint.num_generator_k_bit import num_generator_k_bit
from num_generator_with_randint.num_generator_getrandbits import num_generator_getrandbits

print(f"{'Bit sizes':<10}{'Time1(ms)':<22}{'Time2(ms)':<15}")
print("=" * 40)

bit_sizes = [8, 16, 32, 64, 128, 256, 512, 1024]
repeats = 10000

for bit in bit_sizes:
    randint_time_exec = timeit.timeit(lambda: num_generator_k_bit(bit), number=repeats) * 1000
    getrandbits_time_exec = timeit.timeit(lambda: num_generator_getrandbits(bit), number=repeats) * 1000

    print(f"{bit:<10}{randint_time_exec / repeats:<15.6f}{getrandbits_time_exec / repeats:15.6f}")


