st = "89,35,67,88,abc,66,87"

nums = [int(n) for n in st.split(",") if n.isdigit()]
print(sum(nums))

