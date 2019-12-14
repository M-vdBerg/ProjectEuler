# Problem 3 / Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

base = 600851475143
divisor = 2

while base != divisor:
    if base % divisor == 0:
        base = base / divisor
        continue
    else:
        divisor += 1
print(divisor)
