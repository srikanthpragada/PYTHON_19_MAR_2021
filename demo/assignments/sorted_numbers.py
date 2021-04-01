
st = "10,25,60,9,55,100"
# nums = []
# for v in st.split(","):
#     nums.append(int(v))

nums = [int(v) for v in st.split(",")]

for n in sorted(nums):
    print(n)
