def unique_factors(*nums):
    factors = set()
    for n in nums:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                factors.add(i)

    return sorted(factors)


print(unique_factors(15, 30, 75))
print(unique_factors(10, 30, 24,98,123))
