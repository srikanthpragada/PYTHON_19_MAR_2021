nums = [-10, 10, 5, 6, -80, -4, 2]

for n in sorted(nums, key = lambda v : -v if v < 0 else v):
    print(n)
