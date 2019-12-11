# Problem 5 / Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


found = False
number = 1


def divisible(i):
    if i % 1000000 == 0:
        print(i)
    div = True
    # running quite long for values 1-20
    for divisor in range(1, 21):
        div &= number % divisor == 0
    return div


while not found:
    if not divisible(number):
        number += 1
    else:
        found = True
print(number)
