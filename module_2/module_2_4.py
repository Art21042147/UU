numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for number in numbers[1:]:
    for divisor in range(2, number):
        if number % divisor == 0:
            not_primes.append(number)
            break
    else:
        primes.append(number)

print(f'Primes: {primes}\nNot primes: {not_primes}')
