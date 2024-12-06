numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_primes = 0
for i in range(len(numbers)):
    is_primes = True
    print(numbers[i])
    for j in range(2, i + 2):
        print(j)
        if i % j == 0:
            is_primes = False
            primes.append(numbers[i])
        if is_primes:
            not_primes.append(numbers[i])
        break
    print(not_primes)
    print(primes)