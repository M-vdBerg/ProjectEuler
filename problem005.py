# Problem 5 / Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def prime_factors(z):
    divisor = 2
    divisors = {}
    while z != divisor:
        if z % divisor == 0:
            z = z / divisor
            if divisor in divisors:
                divisors[divisor] = divisors[divisor] + 1
            else:
                divisors[divisor] = 1

            continue
        else:
            divisor += 1
    if divisor in divisors:
        divisors[divisor] = divisors[divisor] + 1
    else:
        divisors[divisor] = 1
    return divisors


def max_power(numbers):
    max_pow = {}
    for divisor in numbers:
        tmp = prime_factors(divisor)
        for i in sorted(tmp):
            if i not in max_pow or max_pow[i] < tmp[i]:
                max_pow[i] = tmp[i]
    return max_pow


min_divisible = 1
max_powers = max_power(range(2, 21))
for prime_factor in list(max_powers):
    min_divisible *= prime_factor.__pow__(max_powers[prime_factor])
print(min_divisible)
