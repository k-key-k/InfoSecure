import timeit
from Evklid.gcd_finder import gcd_finder
from num_generator_with_randint.num_generator_k_bit import num_generator_k_bit

print(f"{'Bit sizes':<10}{'Time (ms)':<10}")
print("=" * 20)

bit_sizes = [8, 16, 32, 64, 128, 256, 512, 1024]

for bit in bit_sizes:
    def test():
        a = num_generator_k_bit(bit)
        b = num_generator_k_bit(bit)
        gcd_finder(a, b)


    exec_time = timeit.timeit(test, number=1000) * 1000
    print(f"{bit:<10}{exec_time:10.6f}")
