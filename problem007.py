# Problem 7 / 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import math


def is_prime(z):
    for i in range(2, math.sqrt(z).__int__() + 1):
        if z % i == 0:
            return False
    return True


number = 2
count = 0
while True:
    if is_prime(number):
        count += 1
        if count > 10000:
            break
    number += 1
print(number)
