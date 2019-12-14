# Problem 10 / Summation of primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import math


def is_prime(z):
    for i in range(2, math.sqrt(z).__int__() + 1):
        if z % i == 0:
            return False
    return True


number = 2
sum_of_primes = 0
while number < 2000000:
    if is_prime(number):
        sum_of_primes += number
    number += 1
print(sum_of_primes)
