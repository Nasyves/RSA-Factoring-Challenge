import sys
import math

def factorize(number):
    factors = []
    sqrt = int(math.sqrt(number)) + 1
    for i in range(2, sqrt):
        if number % i == 0:
            factors.append((i, number // i))
    return factors

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readlines()
        for number in numbers:
            number = int(number.strip())
            factors = factorize(number)
            for factor in factors:
                print(f"{number}={factor[0]}*{factor[1]}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: factors <file>")
    else:
        file_path = sys.argv[1]
        factorize_file(file_path)
