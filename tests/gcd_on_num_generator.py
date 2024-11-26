from Evklid.gcd_finder import gcd_finder
from num_generator_with_randint.num_generator_k_bit import num_generator_k_bit

k = int(input("Введите битность для генерации двух чисел: "))

num1 = num_generator_k_bit(k)
num2 = num_generator_k_bit(k)

result = gcd_finder(num1, num2)

print(f"Наибольший общий делитель для {num1} и {num2} - {result}")