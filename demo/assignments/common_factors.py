def common_factors(*nums):
    min_num = min(nums)  # Find out min of all values

    factors = []
    for i in range(2, min_num // 2 + 1):
        for v in nums:
            if v % i != 0:
                break  # Stop if a number is not divisible
        else:
            factors.append(i)  # Add if all numbers are divisible by i

    return factors


print(common_factors(15, 30, 75))
print(common_factors(10, 30, 24, 98))
