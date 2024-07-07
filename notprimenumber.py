def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_prime_digits_only(num):
    for digit in str(num):
        if digit not in {'2', '3', '5', '7'}:
            return False
    return True

def not_primes(a, b):
    result = []
    for num in range(a, b):
        if is_prime_digits_only(num) and not is_prime(num):
            result.append(num)
    return result

# Example Usage
a = 100
b = 1000
result = not_primes(a, b)
print(result)
