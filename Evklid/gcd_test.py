from Evklid.gcd_finder import gcd_finder

num1 = int(input("Enter big integer num: "))
num2 = int(input("Enter big integer num: "))

result = gcd_finder(num1, num2)

print(f"gcd of {num1} and {num2} is {result}")