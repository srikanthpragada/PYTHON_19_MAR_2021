def nexteven(n):
    return n + 2 if n % 2 == 0 else n + 1


nums = [10, 20, 11, 15, 30]

for v in map(nexteven, nums):
    print(v)
