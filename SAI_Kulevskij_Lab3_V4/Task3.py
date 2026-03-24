def get_primes(n):
    primes = []
    for num in range(2, n + 1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

def find_prime_partitions(target, primes, start_index, current_partition, all_partitions):
    if target == 0:
        all_partitions.append(list(current_partition))
        return

    for i in range(start_index, len(primes)):
        p = primes[i]
        if p <= target:
            current_partition.append(p)
            find_prime_partitions(target - p, primes, i, current_partition, all_partitions)
            current_partition.pop()

def solve(n):
    if n < 2:
        return []
    primes = get_primes(n)
    results = []
    find_prime_partitions(n, primes, 0, [], results)
    return results

number = int(input("Введіть число (до 20): "))
combinations = solve(number)

print(f"\nСпособи розбити число {number} на суму простих чисел:")
for combo in combinations:
    print(" + ".join(map(str, combo)))

print(f"\nЗагальна кількість способів: {len(combinations)}")